from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db

from models.admin import Admin

from authentication.auth import (
    verify_password,
    create_access_token
)

from authentication.schemas import LoginRequest

router = APIRouter(
    prefix="/admin",
    tags=["Admin Authentication"]
)


@router.post("/login")
def admin_login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    # Find Admin
    admin = db.query(Admin).filter(
        Admin.email == request.email
    ).first()

    # Check Email
    if admin is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Admin Email"
        )

    # Check Password
    if not verify_password(
        request.password,
        admin.password
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Admin Password"
        )

    # Create JWT Token
    access_token = create_access_token(
        data={
            "sub": admin.email,
            "role": "admin",
            "id": admin.id
        }
    )

    # Success Response
    return {

        "message": "Admin Login Successful",

        "access_token": access_token,

        "token_type": "bearer",

        "admin_id": admin.id,

        "name": admin.name,

        "email": admin.email,

        "role": "admin"

    }