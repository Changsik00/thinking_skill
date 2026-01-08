# agents/graph.py
import os
from dotenv import load_dotenv
from typing import Literal

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, START, END

from agents.state import AgentState
from agents.prompts import CREATIVE_SYSTEM_PROMPT, CRITICAL_SYSTEM_PROMPT

# Load Environment Variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

# Initialize Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    google_api_key=api_key,
    temperature=0.7
)

# --- Node Definitions ---

def creative_node(state: AgentState):
    """
    Creative Agent Node:
    Generates ideas based on user input.
    """
    messages = state["messages"]
    # System Prompt injection for this turn
    system_message = SystemMessage(content=CREATIVE_SYSTEM_PROMPT)
    
    # Check if system prompt is already there? 
    # For simplicity, we just pass [System, ...Messages] to LLM.
    # But since messages in state accumulate, we should construct the input carefully.
    
    response = llm.invoke([system_message] + messages)
    # The response is an AIMessage. We can optionally tag it with name="creative"
    response.name = "creative"
    
    return {"messages": [response]}

def critical_node(state: AgentState):
    """
    Critical Agent Node:
    Critiques the ideas from Creative Agent.
    """
    messages = state["messages"]
    system_message = SystemMessage(content=CRITICAL_SYSTEM_PROMPT)
    
    response = llm.invoke([system_message] + messages)
    response.name = "critical"
    
    return {"messages": [response]}

# --- Graph Definition ---

workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("creative", creative_node)
workflow.add_node("critical", critical_node)

# Add Edges (Linear Flow for MVP)
workflow.add_edge(START, "creative")
workflow.add_edge("creative", "critical")
workflow.add_edge("critical", END)

# Compile
graph = workflow.compile()
