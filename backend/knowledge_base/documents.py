from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from models.knowledge_base import KnowledgeBase

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge Base"]
)


@router.get("/documents")
def get_documents(db: Session = Depends(get_db)):
    documents = db.query(KnowledgeBase).all()

    return {
        "total_documents": len(documents),
        "documents": documents
    }