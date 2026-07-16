import os
from langchain_community.document_loaders import PyPDFLoader

UPLOAD_FOLDER = "uploads"


def load_documents():

    documents = []

    for file in os.listdir(UPLOAD_FOLDER):

        if file.endswith(".pdf"):

            path = os.path.join(
                UPLOAD_FOLDER,
                file
            )

            loader = PyPDFLoader(path)

            documents.extend(loader.load())

    return documents