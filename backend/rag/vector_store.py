from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embeddings):

    vector_db = FAISS.from_documents(

        chunks,

        embeddings

    )

    vector_db.save_local("vector_db")

    return vector_db