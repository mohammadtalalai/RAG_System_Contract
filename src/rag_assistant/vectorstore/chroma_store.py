from __future__ import annotations
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings

_COLLECTION_NAME = "rag_docs"

def get_chroma_store(embeddings: Embeddings, persist_directory: str) -> Chroma:
    return Chroma(
        collection_name=_COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=persist_directory,
    )