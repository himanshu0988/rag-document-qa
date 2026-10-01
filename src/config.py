import os

from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:

    raise ValueError(
        "OPENAI_API_KEY is not set. "
        "Please add it to the .env file."
    )


DOCUMENTS_PATH = "data/documents"

VECTORSTORE_PATH = "vectorstore/faiss_index"


CHUNK_SIZE = 1500

CHUNK_OVERLAP = 300

TOP_K = 6


EMBEDDING_MODEL = "text-embedding-3-small"

LLM_MODEL = "gpt-4o-mini"