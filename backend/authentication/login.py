from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from models.user import User

from authentication.auth import (
    verify_password,
    create_access_token
)

from authentication.schemas import LoginRequest

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login_user(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    # Check if user exists
    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email"
        )

    # Verify password
    if not verify_password(
        request.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    # Create JWT Token
    access_token = create_access_token(
        data={
            "sub": user.email,
            "id": user.id,
            "role": user.role
        }
    )

    # Return Login Response
    return {

        "message": "Login Successful",

        "access_token": access_token,

        "token_type": "bearer",

        "user_id": user.id,

        "name": user.name,

        "email": user.email,

        "role": user.role,

        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }

    }