import os
import pytest
from rag_assistant.settings import settings
from rag_assistant.ingestion.ingest import ingest_pdfs
from rag_assistant.rag.chain import build_rag_chain

@pytest.mark.skipif(not os.path.exists(settings.test_data_dir), reason="test_data dir missing")
def test_rag_smoke():
    result = ingest_pdfs(settings.test_data_dir)
    if not result.get("ok"):
        pytest.skip("No PDFs in test_data")

    chain = build_rag_chain()
    out = chain.invoke({"question": "What is this document about?", "summary": ""})
    assert "answer" in out and isinstance(out["answer"], str)