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


class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    issue = Column(Text)

    status = Column(String(50))

    assigned_agent = Column(String(100))

    priority = Column(String(20))

    created_at = Column(
        DateTime,
        default=func.now()
    )