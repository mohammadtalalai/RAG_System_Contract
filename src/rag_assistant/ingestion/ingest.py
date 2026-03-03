from __future__ import annotations
import logging
from langchain_core.documents import Document

from rag_assistant.settings import settings
from rag_assistant.utils import ensure_dir, list_pdfs
from rag_assistant.ingestion.loaders import load_pdf
from rag_assistant.ingestion.chunking import chunk_documents
from rag_assistant.llm.embeddings import get_embeddings
from rag_assistant.vectorstore.chroma_store import get_chroma_store

logger = logging.getLogger(__name__)

def ingest_pdfs(input_dir: str | None = None) -> dict:
    input_dir = input_dir or settings.test_data_dir
    pdfs = list_pdfs(input_dir)
    if not pdfs:
        return {"ok": False, "message": f"No PDFs found in {input_dir}"}

    ensure_dir(settings.chroma_dir)

    all_pages: list[Document] = []
    for pdf in pdfs:
        pages = load_pdf(pdf)
        for p in pages:
            p.metadata = dict(p.metadata or {})
            p.metadata["source"] = pdf
        all_pages.extend(pages)

    chunks = chunk_documents(all_pages, settings.chunk_size, settings.chunk_overlap)

    embeddings = get_embeddings()
    store = get_chroma_store(embeddings=embeddings, persist_directory=settings.chroma_dir)

    store.add_documents(chunks)
    store.persist()

    logger.info("Ingested %d PDFs, %d pages, %d chunks", len(pdfs), len(all_pages), len(chunks))
    return {
        "ok": True,
        "pdf_count": len(pdfs),
        "page_count": len(all_pages),
        "chunk_count": len(chunks),
        "persist_dir": settings.chroma_dir,
    }