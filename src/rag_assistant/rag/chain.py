from __future__ import annotations
from typing import Any
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from rag_assistant.settings import settings
from rag_assistant.llm.models import get_chat_model
from rag_assistant.llm.embeddings import get_embeddings
from rag_assistant.vectorstore.chroma_store import get_chroma_store
from rag_assistant.rag.prompts import RAG_PROMPT
from rag_assistant.rag.citations import format_docs_with_citations

def build_rag_chain() -> Any:
    llm = get_chat_model(temperature=0.0)
    embeddings = get_embeddings()
    store = get_chroma_store(embeddings=embeddings, persist_directory=settings.chroma_dir)
    retriever = store.as_retriever(search_kwargs={"k": settings.top_k})

    def retrieve(inputs: dict) -> dict:
        q = inputs["question"]
        docs = retriever.get_relevant_documents(q)
        return {"docs": docs}

    chain = (
        RunnablePassthrough.assign(**{"retrieved": RunnableLambda(retrieve)})
        .assign(context=lambda x: format_docs_with_citations(x["retrieved"]["docs"]))
        .assign(answer=(RAG_PROMPT | llm | StrOutputParser()))
    )
    return chain