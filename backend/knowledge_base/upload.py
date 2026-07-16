import os
import shutil

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from models.knowledge_base import KnowledgeBase

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge Base"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
def upload_document(
    title: str,
    category: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = KnowledgeBase(
        title=title,
        category=category,
        file_name=file.filename
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "Document Uploaded Successfully",
        "document_id": document.id,
        "file_name": file.filename
    }