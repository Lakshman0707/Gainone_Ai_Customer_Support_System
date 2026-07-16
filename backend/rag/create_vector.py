from rag.document_loader import load_documents
from rag.text_splitter import split_documents
from rag.embeddings import get_embedding_model
from rag.vector_store import create_vector_store


def main():

    print("Loading PDFs...")

    documents = load_documents()

    print(f"Loaded {len(documents)} pages")

    print("Splitting Documents...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Loading Embedding Model...")

    embeddings = get_embedding_model()

    print("Creating FAISS Vector Database...")

    create_vector_store(
        chunks,
        embeddings
    )

    print("Vector Database Created Successfully")


if __name__ == "__main__":
    main()