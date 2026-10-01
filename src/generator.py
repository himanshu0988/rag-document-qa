from langchain_openai import ChatOpenAI

from src.config import LLM_MODEL


def create_llm():

    return ChatOpenAI(
        model=LLM_MODEL
    )