# agents/state.py
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """
    LangGraph의 상태를 정의합니다.
    - messages: 대화 히스토리 (add_messages 리듀서 사용)
    """
    messages: Annotated[List[BaseMessage], add_messages]
