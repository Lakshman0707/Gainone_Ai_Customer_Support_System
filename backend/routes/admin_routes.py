from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db

from models.user import User
from models.ticket import Ticket
from models.chat_history import ChatHistory
from models.knowledge_base import KnowledgeBase

router = APIRouter(
    prefix="/admin",
    tags=["Admin Dashboard"]
)

# ==========================================
# Dashboard
# ==========================================

@router.get("/dashboard")
def admin_dashboard(db: Session = Depends(get_db)):

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


# ==========================================
# All Customers
# ==========================================

@router.get("/customers")
def get_all_customers(db: Session = Depends(get_db)):

    users = db.query(User).all()

    result = []

    for user in users:

        chat_count = db.query(ChatHistory).filter(
            ChatHistory.user_id == user.id
        ).count()

        ticket_count = db.query(Ticket).filter(
            Ticket.user_id == user.id
        ).count()

        result.append({

            "id": user.id,

            "name": user.name,

            "email": user.email,

            "role": user.role,

            "total_chats": chat_count,

            "total_tickets": ticket_count

        })

    return result


# ==========================================
# Customer Details
# ==========================================

@router.get("/customer/{user_id}")
def customer_details(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:

        return {

            "message": "Customer Not Found"

        }

    ticket_count = db.query(Ticket).filter(
        Ticket.user_id == user.id
    ).count()

    chat_count = db.query(ChatHistory).filter(
        ChatHistory.user_id == user.id
    ).count()

    return {

        "id": user.id,

        "name": user.name,

        "email": user.email,

        "role": user.role,

        "total_chats": chat_count,

        "total_tickets": ticket_count

    }


# ==========================================
# Customer Chat History
# ==========================================

@router.get("/customer/{user_id}/history")
def customer_history(
    user_id: int,
    db: Session = Depends(get_db)
):

    history = db.query(ChatHistory).filter(

        ChatHistory.user_id == user_id

    ).order_by(

        ChatHistory.created_at.desc()

    ).all()

    result = []

    for chat in history:

        result.append({

            "question": chat.question,

            "answer": chat.response,

            "session_id": chat.session_id,

            "created_at": chat.created_at

        })

    return result


# ==========================================
# All Tickets
# ==========================================

@router.get("/tickets")
def get_all_tickets(
    db: Session = Depends(get_db)
):

    tickets = db.query(Ticket).all()

    result = []

    for ticket in tickets:

        user = db.query(User).filter(
            User.id == ticket.user_id
        ).first()

        result.append({

            "ticket_id": ticket.id,

            "customer": user.name if user else "Unknown",

            "email": user.email if user else "",

            "issue": ticket.issue,

            "status": ticket.status,

            "priority": ticket.priority,

            "assigned_agent": ticket.assigned_agent,

            "created_at": ticket.created_at

        })

    return result