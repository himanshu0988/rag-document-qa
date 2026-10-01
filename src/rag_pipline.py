from src.embeddings import create_embeddings
from src.vector_store import load_vector_store
from src.retriever import create_retriever
from src.prompt import create_prompt
from src.generator import create_llm


def create_rag_pipeline(file_name=None):

    embeddings = create_embeddings()

    vector_store = load_vector_store(
        embeddings
    )

    retriever = create_retriever(
        vector_store,
        file_name
    )

    prompt = create_prompt()

    llm = create_llm()

    return retriever, prompt, llm


def answer_question(
    question,
    retriever,
    prompt,
    llm
):

    documents = retriever.invoke(
        question
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    messages = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(
        messages
    )

    return response.content, documents