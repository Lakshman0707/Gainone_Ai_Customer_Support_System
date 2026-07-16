from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from models.knowledge_base import KnowledgeBase

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge Base"]
)


@router.get("/search")
def search_document(
    keyword: str,
    db: Session = Depends(get_db)
):

    documents = db.query(KnowledgeBase).filter(
        KnowledgeBase.title.contains(keyword)
    ).all()

    return {
        "keyword": keyword,
        "results": documents
    }