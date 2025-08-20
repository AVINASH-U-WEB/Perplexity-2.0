from typing import Dict, Any, List, TypedDict
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: List[BaseMessage]
    # Add any other state properties you need