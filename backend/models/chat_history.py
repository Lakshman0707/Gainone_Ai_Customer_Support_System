from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func

from app.database import Base


class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    question = Column(Text)

    response = Column(Text)

    session_id = Column(String(100))

    created_at = Column(
        DateTime,
        default=func.now()
    )