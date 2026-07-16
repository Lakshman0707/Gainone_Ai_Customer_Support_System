from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.sql import func

from app.database import Base


class KnowledgeBase(Base):

    __tablename__ = "knowledge_base"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    category = Column(String(100))

    file_name = Column(String(255))

    uploaded_at = Column(
        DateTime,
        default=func.now()
    )