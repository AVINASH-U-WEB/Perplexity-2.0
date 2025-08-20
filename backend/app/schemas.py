from pydantic import BaseModel
from typing import List, Literal, Optional

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    thread_id: Optional[str] = None

class ChatResponse(BaseModel):
    thread_id: str
    response: str