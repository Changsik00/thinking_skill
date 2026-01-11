# app/infrastructure/llm/langgraph_adapter.py
import os
from typing import TypedDict, Annotated, List, Optional, Dict, Any
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
import operator

from app.domain.interfaces import ThinkingBrain, MemoryVault
from app.domain.entities import DebateResult
from app.infrastructure.llm.prompts import CREATIVE_SYSTEM_PROMPT, CRITICAL_SYSTEM_PROMPT

# --- Local State Definition (Internal to this adapter) ---
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]

class LangGraphBrain(ThinkingBrain):
    """
    Implementation of ThinkingBrain using LangGraph and Gemini.
    """
    def __init__(self, memory: Optional[MemoryVault] = None, nerve: Optional[Any] = None):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set in .env")
        
        self.memory = memory
        self.nerve = nerve  # N8nAdapter (NerveSystem)
        
        # Default model from env or fallback
        self.default_model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-2.0-flash-001")
        self.graph = self._build_graph()

    def _get_llm(self, config: RunnableConfig) -> ChatGoogleGenerativeAI:
        """
        Factory to get LLM instance based on config or default.
        """
        model_name = self.default_model_name
        if config and "configurable" in config:
            model_name = config["configurable"].get("model_name", self.default_model_name)
            
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=self.api_key,
            temperature=0.7
        )
        
        # Bind tools if available
        tools = []
        if self.memory:
            tools.append(self._create_save_tool())
        if self.nerve:
            tools.append(self._create_automation_tool())
            
        if tools:
            return llm.bind_tools(tools)
        
        return llm

    def _create_save_tool(self):
        """Creates the save_debate tool bound to the memory vault."""
        
        @tool("save_debate")
        def save_debate(topic: str, content: str) -> str:
            """
            Save the debate/discussion content to the permanent memory (Obsidian/ChromaDB).
            Use this when the user asks to save, or when the discussion reaches a valuable conclusion.
            """
            if not self.memory:
                return "Memory system is not connected."
            
            try:
                result = DebateResult(topic=topic, content=content, model="System")
                path = self.memory.save(result)
                return f"Successfully saved to {path}"
            except Exception as e:
                return f"Failed to save: {str(e)}"
                
        return save_debate

    def _create_automation_tool(self):
        """Creates the trigger_automation tool bound to the nerve system."""
        
        @tool("trigger_automation")
        def trigger_automation(target: str, content: str) -> str:
            """
            Trigger an external automation workflow via n8n.
            
            Args:
                target: The destination/intent (e.g., 'slack', 'email', 'blog', 'jira').
                content: The summary or content to send.
            """
            if not self.nerve:
                return "Automation system (Nerve) is not connected."
            
            # Create a temporary result object to pass to adapter
            result = DebateResult(topic="Automation Trigger", content=content, model="System")
            return self.nerve.trigger(result, target=target)
            
        return trigger_automation

    def _creative_node(self, state: AgentState, config: RunnableConfig):
        messages = state["messages"]
        # Creative node usually doesn't need to save, but we use _get_llm which binds tools.
        # It's okay if it doesn't use it.
        llm = self._get_llm(config)
        
        system_message = SystemMessage(content=CREATIVE_SYSTEM_PROMPT)
        response = llm.invoke([system_message] + messages)
        response.name = "creative"
        return {"messages": [response]}

    def _critical_node(self, state: AgentState, config: RunnableConfig):
        messages = state["messages"]
        llm = self._get_llm(config)
        
        system_message = SystemMessage(content=CRITICAL_SYSTEM_PROMPT)
        # Explicit trigger for critical agent
        trigger_message = HumanMessage(content="위의 아이디어들을 분석하고 비판해 주세요.")
        
        # We append the trigger only if the last message is NOT from critical agent or tools
        # Actually, in a loop (Critical -> Tool -> Critical), we might want to vary the trigger or omit it.
        # If the last message is a ToolMessage, we usually don't need to re-trigger "analyze this".
        # The LLM knows it just called a tool.
        
        input_messages = [system_message] + messages
        if not isinstance(messages[-1], ToolMessage) and messages[-1].name != "critical":
             input_messages.append(trigger_message)
             
        response = llm.invoke(input_messages)
        response.name = "critical"
        return {"messages": [response]}

    def _build_graph(self):
        workflow = StateGraph(AgentState)
        workflow.add_node("creative", self._creative_node)
        workflow.add_node("critical", self._critical_node)
        
        workflow.add_edge(START, "creative")
        workflow.add_edge("creative", "critical")
        
        # Collect tools
        tools = []
        if self.memory:
            tools.append(self._create_save_tool())
        if self.nerve:
            tools.append(self._create_automation_tool())
            
        # If tools enabled, add ToolNode and Conditional Edges
        if tools:
            workflow.add_node("tools", ToolNode(tools))
            
            workflow.add_conditional_edges(
                "critical",
                tools_condition,
            )
            workflow.add_edge("tools", "critical")
        else:
            workflow.add_edge("critical", END)
        
        return workflow.compile()

    def think(self, topic: str, model_name: Optional[str] = None) -> str:
        """
        Executes the graph and returns the final response content.
        """
        initial_state = {"messages": [HumanMessage(content=topic)]}
        config = {"configurable": {"model_name": model_name}} if model_name else None
        
        result = self.graph.invoke(initial_state, config=config)
        
        # Extract the last message content (Critical Agent's response)
        last_message = result["messages"][-1]
        
        return last_message.content

    async def think_stream(self, topic: str, model_name: Optional[str] = None):
        """
        Executes the graph and yields tokens from the LLM.
        """
        initial_state = {"messages": [HumanMessage(content=topic)]}
        config = {"configurable": {"model_name": model_name}} if model_name else None
        
        # Use astream_events to get real-time tokens
        # version="v1" is required for stability
        async for event in self.graph.astream_events(initial_state, config=config, version="v1"):
            kind = event["event"]
            
            # Filter for LLM streaming events
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    yield content

