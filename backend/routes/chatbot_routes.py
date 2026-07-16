from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from chatbot.chatbot import ask_chatbot
from chatbot.response import (
    ChatRequest,
    ChatResponse
)

router = APIRouter(
    prefix="/chatbot",
    tags=["AI Chatbot"]
)


@router.post(
    "/ask",
    response_model=ChatResponse
)
def chatbot(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    return ask_chatbot(
        db=db,
        user_id=request.user_id,
        question=request.question
    )