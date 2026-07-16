from sqlalchemy.orm import Session

from models.chat_history import ChatHistory


def get_chat_history(
    db: Session,
    user_id: int
):

    chats = db.query(ChatHistory).filter(

        ChatHistory.user_id == user_id

    ).order_by(

        ChatHistory.created_at.desc()

    ).all()

    return chats