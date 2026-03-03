from __future__ import annotations
from langchain_core.documents import Document
from rag_assistant.utils import safe_filename

def format_docs_with_citations(docs: list[Document], max_chars: int = 12000) -> str:
    parts: list[str] = []
    total = 0
    for d in docs:
        source = safe_filename(d.metadata.get("source", "unknown"))
        page = d.metadata.get("page", "NA")
        chunk_id = d.metadata.get("chunk_id", "NA")
        header = f"[{source}:{page} | chunk:{chunk_id}]"
        text = d.page_content.strip()
        block = f"{header}\n{text}\n"
        total += len(block)
        if total > max_chars:
            break
        parts.append(block)
    return "\n".join(parts)