from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from src.config import DOCUMENTS_PATH


def load_documents():
    documents = []

    pdf_files = sorted(
        Path(DOCUMENTS_PATH).glob("*.pdf")
    )

    for pdf_file in pdf_files:

        loader = PyPDFLoader(
            str(pdf_file)
        )

        pdf_documents = loader.load()

        for document in pdf_documents:

            document.metadata["file_name"] = (
                pdf_file.name
            )

        documents.extend(pdf_documents)

    if not documents:

        raise FileNotFoundError(
            f"No PDF documents found in {DOCUMENTS_PATH}"
        )

    return documents