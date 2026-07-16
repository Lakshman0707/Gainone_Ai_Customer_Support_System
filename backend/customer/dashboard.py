from sqlalchemy.orm import Session

from models.chat_history import ChatHistory
from models.ticket import Ticket


def customer_dashboard(
    db: Session,
    user_id: int
):

    total_chats = db.query(ChatHistory).filter(
        ChatHistory.user_id == user_id
    ).count()

    total_tickets = db.query(Ticket).filter(
        Ticket.user_id == user_id
    ).count()

    return {

        "total_chats": total_chats,

        "total_tickets": total_tickets

    }