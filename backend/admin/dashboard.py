from sqlalchemy.orm import Session

from models.user import User
from models.ticket import Ticket
from models.chat_history import ChatHistory
from models.knowledge_base import KnowledgeBase


def dashboard_summary(db: Session):

    total_users = db.query(User).count()

    total_tickets = db.query(Ticket).count()

    total_chats = db.query(ChatHistory).count()

    total_documents = db.query(KnowledgeBase).count()

    return {

        "total_users": total_users,

        "total_tickets": total_tickets,

        "total_chats": total_chats,

        "total_documents": total_documents

    }