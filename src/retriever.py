from src.config import TOP_K


def create_retriever(vector_store, file_name=None):

    search_kwargs = {
        "k": TOP_K
    }

    if file_name:
        search_kwargs["filter"] = {
            "file_name": file_name
        }

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs=search_kwargs
    )