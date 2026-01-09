# app/infrastructure/llm/langgraph_adapter.py
import os
from typing import TypedDict, Annotated, List
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
import operator

from app.domain.interfaces import ThinkingBrain
from app.infrastructure.llm.prompts import CREATIVE_SYSTEM_PROMPT, CRITICAL_SYSTEM_PROMPT

# --- Local State Definition (Internal to this adapter) ---
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]

class LangGraphBrain(ThinkingBrain):
    """
    Implementation of ThinkingBrain using LangGraph and Gemini.
    """
    def __init__(self, model_name: str = "gemini-2.0-flash-001"):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set in .env")
        
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=0.7
        )
        self.graph = self._build_graph()

    def _creative_node(self, state: AgentState):
        messages = state["messages"]
        system_message = SystemMessage(content=CREATIVE_SYSTEM_PROMPT)
        response = self.llm.invoke([system_message] + messages)
        response.name = "creative"
        return {"messages": [response]}

    def _critical_node(self, state: AgentState):
        messages = state["messages"]
        system_message = SystemMessage(content=CRITICAL_SYSTEM_PROMPT)
        # Explicit trigger for critical agent
        trigger_message = HumanMessage(content="위의 아이디어들을 분석하고 비판해 주세요.")
        response = self.llm.invoke([system_message] + messages + [trigger_message])
        response.name = "critical"
        return {"messages": [response]}

    def _build_graph(self):
        workflow = StateGraph(AgentState)
        workflow.add_node("creative", self._creative_node)
        workflow.add_node("critical", self._critical_node)
        
        workflow.add_edge(START, "creative")
        workflow.add_edge("creative", "critical")
        workflow.add_edge("critical", END)
        
        return workflow.compile()

    def think(self, topic: str) -> str:
        """
        Executes the graph and returns the final response content.
        """
        initial_state = {"messages": [HumanMessage(content=topic)]}
        result = self.graph.invoke(initial_state)
        
        # Extract the last message content (Critical Agent's response)
        last_message = result["messages"][-1]
        
        return last_message.content
