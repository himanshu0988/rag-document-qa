from langchain_openai import OpenAIEmbeddings

from src.config import EMBEDDING_MODEL


def create_embeddings():
    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL
    )