from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# ==========================================
# Database Models
# ==========================================

from models.user import User
from models.admin import Admin
from models.ticket import Ticket
from models.chat_history import ChatHistory
from models.knowledge_base import KnowledgeBase

# ==========================================
# Authentication
# ==========================================

from authentication.register import router as register_router
from authentication.login import router as login_router
from authentication.admin_login import router as admin_login_router

# ==========================================
# User
# ==========================================

from routes.user_routes import router as user_router
from routes.customer_routes import router as customer_router

# ==========================================
# Knowledge Base
# ==========================================

from knowledge_base.upload import router as upload_router
from knowledge_base.documents import router as documents_router
from knowledge_base.search import router as search_router

# ==========================================
# AI Chatbot
# ==========================================

from routes.chatbot_routes import router as chatbot_router

# ==========================================
# Conversations
# ==========================================

from routes.conversation_routes import router as conversation_router

# ==========================================
# Tickets
# ==========================================

from routes.ticket_routes import router as ticket_router

# ==========================================
# Admin
# ==========================================

from routes.admin_routes import router as admin_router

# ==========================================
# Create Database Tables
# ==========================================

Base.metadata.create_all(bind=engine)

# ==========================================
# FastAPI App
# ==========================================

app = FastAPI(
    title="GainOne AI Customer Support System",
    version="1.0.0",
    description="AI Powered Customer Support using FastAPI + RAG + Groq"
)

# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Register Routers
# ==========================================

# Authentication
app.include_router(register_router)
app.include_router(login_router)
app.include_router(admin_login_router)

# Customer
app.include_router(user_router)
app.include_router(customer_router)

# Knowledge Base
app.include_router(upload_router)
app.include_router(documents_router)
app.include_router(search_router)

# AI Chatbot
app.include_router(chatbot_router)

# Conversation
app.include_router(conversation_router)

# Tickets
app.include_router(ticket_router)

# Admin Dashboard
app.include_router(admin_router)

# ==========================================
# Home
# ==========================================

@app.get("/")
def home():
    return {
        "project": "GainOne AI Customer Support System",
        "version": "1.0.0",
        "status": "Running Successfully"
    }

# ==========================================
# Health
# ==========================================

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }