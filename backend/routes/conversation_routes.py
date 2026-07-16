from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from conversations.save_chat import save_chat
from conversations.history import get_chat_history
from conversations.delete_chat import delete_chat

from models.user import User
from models.chat_history import ChatHistory

from services.summary_service import generate_summary
from services.email_service import send_support_email

router = APIRouter(
    prefix="/conversation",
    tags=["Conversation"]
)

# ==========================================
# Save Chat
# ==========================================

@router.post("/save")
def save_conversation(

    user_id: int,
    question: str,
    response: str,
    session_id: str,

    db: Session = Depends(get_db)

):

    chat = save_chat(

        db=db,

        user_id=user_id,

        question=question,

        response=response,

        session_id=session_id

    )

    return {

        "message": "Conversation Saved",

        "chat_id": chat.id

    }


# ==========================================
# Get Chat History
# ==========================================

@router.get("/history/{user_id}")
def history(

    user_id: int,

    db: Session = Depends(get_db)

):

    chats = get_chat_history(

        db,

        user_id

    )

    return chats


# ==========================================
# Delete Chat
# ==========================================

@router.delete("/delete/{chat_id}")
def delete(

    chat_id: int,

    db: Session = Depends(get_db)

):

    status = delete_chat(

        db,

        chat_id

    )

    if not status:

        raise HTTPException(

            status_code=404,

            detail="Chat Not Found"

        )

    return {

        "message": "Conversation Deleted"

    }


# ==========================================
# Send AI Summary on Customer Logout
# ==========================================

@router.post("/logout-summary/{user_id}")
def logout_summary(

    user_id: int,

    db: Session = Depends(get_db)

):

    user = db.query(User).filter(

        User.id == user_id

    ).first()

    if user is None:

        raise HTTPException(

            status_code=404,

            detail="User Not Found"

        )

    chats = db.query(ChatHistory).filter(

        ChatHistory.user_id == user_id

    ).order_by(

        ChatHistory.created_at.asc()

    ).all()

    if len(chats) == 0:

        return {

            "message": "No Conversation Found"

        }

    conversation = ""

    for chat in chats:

        conversation += f"""

Question:
{chat.question}

Answer:
{chat.response}

"""

    summary = generate_summary(conversation)

    email_status = send_support_email(

        customer_name=user.name,

        customer_email=user.email,

        summary=summary

    )

    if email_status:

        return {

            "message": "Conversation Summary Sent Successfully"

        }

    else:

        raise HTTPException(

            status_code=500,

            detail="Unable to Send Email"

        )