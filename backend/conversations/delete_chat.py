from sqlalchemy.orm import Session

from models.chat_history import ChatHistory


def delete_chat(
    db: Session,
    chat_id: int
):

    chat = db.query(ChatHistory).filter(

        ChatHistory.id == chat_id

    ).first()

    if not chat:

        return False

    db.delete(chat)

    db.commit()

    return True