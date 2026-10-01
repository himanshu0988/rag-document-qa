
from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store


def main():

    print("Loading documents...")

    documents = load_documents()

    print(
        f"Loaded {len(documents)} document pages."
    )


    print("Splitting documents into chunks...")

    chunks = split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks."
    )


    print("Creating embeddings...")

    embeddings = create_embeddings()


    print("Creating FAISS vector store...")

    create_vector_store(
        chunks,
        embeddings
    )


    print(
        "FAISS vector store created successfully."
    )


if __name__ == "__main__":
    main()