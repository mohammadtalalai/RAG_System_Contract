from __future__ import annotations
from langchain_community.embeddings import OllamaEmbeddings
from rag_assistant.settings import settings

def get_embeddings() -> OllamaEmbeddings:
    return OllamaEmbeddings(
        base_url=settings.ollama_base_url,
        model=settings.ollama_embed_model,
    )