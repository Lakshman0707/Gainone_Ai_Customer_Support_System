from uuid import uuid4

from sqlalchemy.orm import Session

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from chatbot.prompt import PROMPT_TEMPLATE
from rag.retriever import get_retriever

from conversations.save_chat import save_chat

from models.user import User
from models.chat_history import ChatHistory

from services.summary_service import generate_summary
from services.email_service import send_support_email

from app.config import (
    GROQ_API_KEY,
    GROQ_MODEL
)

# ==========================================
# Load LLM
# ==========================================

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL
)

# ==========================================
# Human Support Keywords
# ==========================================

HUMAN_KEYWORDS = [

    "human",

    "human support",

    "support",

    "agent",

    "representative",

    "customer care",

    "customer support",

    "talk to human",

    "talk to agent",

    "human interaction",

    "connect me",

    "call me"

]

# ==========================================
# Chatbot Function
# ==========================================

def ask_chatbot(
    db: Session,
    user_id: int,
    question: str
):

    # Load Retriever
    retriever = get_retriever()

    # Retrieve Documents
    documents = retriever.invoke(question)

    # ==========================================
    # Build Context
    # ==========================================

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    # ==========================================
    # Prompt
    # ==========================================

    prompt = ChatPromptTemplate.from_template(
        PROMPT_TEMPLATE
    )

    chain = prompt | llm

    result = chain.invoke({

        "context": context,

        "question": question

    })

    answer = result.content

    # ==========================================
    # Save Chat
    # ==========================================

    session_id = str(uuid4())

    save_chat(

        db=db,

        user_id=user_id,

        question=question,

        response=answer,

        session_id=session_id

    )

    # ==========================================
    # Check Human Support Request
    # ==========================================

    request_human = any(

        keyword in question.lower()

        for keyword in HUMAN_KEYWORDS

    )

    ai_failed = (

        "i don't know" in answer.lower()

        or "not found" in answer.lower()

        or "unable to answer" in answer.lower()

        or "sorry" in answer.lower()

    )

    if request_human or ai_failed:

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        chats = db.query(ChatHistory).filter(
            ChatHistory.user_id == user_id
        ).order_by(
            ChatHistory.created_at.asc()
        ).all()

        conversation = ""

        for chat in chats:

            conversation += f"""

Question:
{chat.question}

Answer:
{chat.response}

"""

        summary = generate_summary(conversation)

        send_support_email(

            customer_name=user.name,

            customer_email=user.email,

            summary=summary

        )

        answer += """

Your request has been forwarded to our human support team.

Our support team will contact you shortly.

"""

    # ==========================================
    # Response
    # ==========================================

    return {

        "question": question,

        "answer": answer,

        "documents_found": len(documents),

        "session_id": session_id

    }