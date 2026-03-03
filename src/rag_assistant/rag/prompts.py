from __future__ import annotations
from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a grounded assistant. Answer ONLY using the provided context.\n"
         "If the answer is not in the context, say you don't know.\n"
         "Always include citations in [source:page] format for key claims."),
        ("system", "Conversation summary (may be empty):\n{summary}"),
        ("human",
         "Question:\n{question}\n\n"
         "Context:\n{context}\n\n"
         "Return:\n"
         "1) Answer\n"
         "2) Citations inline like [file.pdf:3]\n"
         "3) If not found, say: 'I don't know based on the provided document.'")
    ]
)