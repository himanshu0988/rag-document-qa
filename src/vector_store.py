from pathlib import Path

from langchain_community.vectorstores import FAISS

from src.config import VECTORSTORE_PATH


def create_vector_store(chunks, embeddings):

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    Path(VECTORSTORE_PATH).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store.save_local(
        VECTORSTORE_PATH
    )

    return vector_store


def load_vector_store(embeddings):

    if not Path(VECTORSTORE_PATH).exists():

        raise FileNotFoundError(
            "FAISS index not found. Run ingest.py first."
        )

    vector_store = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store