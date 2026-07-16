from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: int
    question: str


class ChatResponse(BaseModel):
    question: str
    answer: str
    documents_found: int
    session_id: str