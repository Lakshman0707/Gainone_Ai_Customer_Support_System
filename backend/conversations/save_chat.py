from sqlalchemy.orm import Session

from models.chat_history import ChatHistory


def save_chat(
    db: Session,
    user_id: int,
    question: str,
    response: str,
    session_id: str
):

    chat = ChatHistory(

        user_id=user_id,

        question=question,

        response=response,

        session_id=session_id

    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat