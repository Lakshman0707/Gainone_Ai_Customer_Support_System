from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embedding_model

VECTOR_DB = "vector_db"


def get_retriever():

    embeddings = get_embedding_model()

    vector_db = FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 5
        }
    )