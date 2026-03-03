from rag_assistant.ingestion.chunking import chunk_documents
from langchain_core.documents import Document

def test_chunking_produces_chunks():
    docs = [Document(page_content="A" * 5000, metadata={"source": "x.pdf", "page": 0})]
    chunks = chunk_documents(docs, chunk_size=1000, chunk_overlap=100)
    assert len(chunks) >= 4
    assert "chunk_id" in chunks[0].metadata