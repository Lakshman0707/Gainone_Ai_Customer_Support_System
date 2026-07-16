from sqlalchemy.orm import Session

from models.knowledge_base import KnowledgeBase


def get_all_documents(db: Session):

    return db.query(KnowledgeBase).all()