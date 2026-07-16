from sqlalchemy.orm import Session

from models.chat_history import ChatHistory


def get_all_conversations(db: Session):

    return db.query(ChatHistory).all()