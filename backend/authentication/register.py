from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app.database import get_db

from models.user import User
from models.ticket import Ticket

from authentication.auth import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


@router.post("/register")
def register_user(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    try:

        # Create User
        new_user = User(
            name=request.name,
            email=request.email,
            password=hash_password(request.password),
            role="customer"
        )

        db.add(new_user)

        # Generate user id without committing
        db.flush()

        # Create Default Ticket
        welcome_ticket = Ticket(
            user_id=new_user.id,
            issue="Welcome to GainOne AI Customer Support",
            status="Open",
            assigned_agent="Nandita",
            priority="Low"
        )

        db.add(welcome_ticket)

        # Commit both together
        db.commit()

        db.refresh(new_user)
        db.refresh(welcome_ticket)

        return {
            "success": True,
            "message": "Registration Successful",
            "user_id": new_user.id,
            "ticket_id": welcome_ticket.id
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )