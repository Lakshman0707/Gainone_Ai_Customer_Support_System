from fastapi import APIRouter, Depends

from authentication.auth import get_current_user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/profile")
def get_profile(current_user=Depends(get_current_user)):
    return {
        "message": "Profile Loaded Successfully",
        "user": current_user
    }

@router.get("/dashboard")
def dashboard(current_user=Depends(get_current_user)):
    return {
        "message": "Welcome to GainOne Dashboard",
        "user": current_user
    }