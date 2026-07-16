from sqlalchemy.orm import Session

from models.chat_history import ChatHistory


def get_my_conversations(
    db: Session,
    user_id: int
):

    return db.query(ChatHistory).filter(

        ChatHistory.user_id == user_id

    ).order_by(

        ChatHistory.created_at.desc()

    ).all()