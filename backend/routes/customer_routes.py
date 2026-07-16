from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from customer.profile import get_profile
from customer.dashboard import customer_dashboard
from customer.conversations import get_my_conversations
from customer.tickets import get_my_tickets

router = APIRouter(
    prefix="/customer",
    tags=["Customer Dashboard"]
)

# ==========================================
# Customer Dashboard
# ==========================================

@router.get("/dashboard/{user_id}")
def dashboard(
    user_id: int,
    db: Session = Depends(get_db)
):

    return customer_dashboard(
        db,
        user_id
    )


# ==========================================
# Customer Profile
# ==========================================

@router.get("/profile/{user_id}")
def profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_profile(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    return user


# ==========================================
# Customer Conversations
# ==========================================

@router.get("/conversations/{user_id}")
def conversations(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_my_conversations(
        db,
        user_id
    )


# ==========================================
# Customer Tickets
# ==========================================

@router.get("/tickets/{user_id}")
def tickets(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_my_tickets(
        db,
        user_id
    )