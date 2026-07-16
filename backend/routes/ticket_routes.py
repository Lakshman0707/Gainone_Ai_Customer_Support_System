from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from models.ticket import Ticket

from tickets.create_ticket import create_ticket
from tickets.assign_ticket import assign_ticket
from tickets.ticket_status import update_ticket_status
from tickets.close_ticket import close_ticket

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

# ==========================================
# Create Ticket
# ==========================================

@router.post("/create")
def create_new_ticket(
    user_id: int,
    issue: str,
    priority: str = "Medium",
    db: Session = Depends(get_db)
):

    ticket = create_ticket(
        db=db,
        user_id=user_id,
        issue=issue,
        priority=priority
    )

    return {
        "message": "Ticket Created Successfully",
        "ticket_id": ticket.id,
        "status": ticket.status
    }


# ==========================================
# Get All Tickets
# ==========================================

@router.get("/all")
def get_all_tickets(
    db: Session = Depends(get_db)
):

    tickets = db.query(Ticket).all()

    return tickets


# ==========================================
# Get Ticket By ID
# ==========================================

@router.get("/{ticket_id}")
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket Not Found"
        )

    return ticket


# ==========================================
# Assign Ticket
# ==========================================

@router.put("/assign")
def assign(
    ticket_id: int,
    agent_name: str,
    db: Session = Depends(get_db)
):

    ticket = assign_ticket(
        db=db,
        ticket_id=ticket_id,
        agent_name=agent_name
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket Not Found"
        )

    return {
        "message": "Ticket Assigned Successfully",
        "ticket": ticket
    }


# ==========================================
# Update Ticket Status
# ==========================================

@router.put("/status")
def update_status(
    ticket_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    ticket = update_ticket_status(
        db=db,
        ticket_id=ticket_id,
        status=status
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket Not Found"
        )

    return {
        "message": "Ticket Status Updated",
        "ticket": ticket
    }


# ==========================================
# Close Ticket
# ==========================================

@router.put("/close")
def close(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    ticket = close_ticket(
        db=db,
        ticket_id=ticket_id
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket Not Found"
        )

    return {
        "message": "Ticket Closed Successfully",
        "ticket": ticket
    }