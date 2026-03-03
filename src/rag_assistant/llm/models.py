from __future__ import annotations
from langchain_community.chat_models import ChatOllama
from rag_assistant.settings import settings

def get_chat_model(temperature: float = 0.0) -> ChatOllama:
    return ChatOllama(
        base_url=settings.ollama_base_url,
        model=settings.ollama_chat_model,
        temperature=temperature,
    )