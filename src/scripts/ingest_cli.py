from __future__ import annotations
import argparse

from rag_assistant.logging_config import setup_logging
from rag_assistant.ingestion.ingest import ingest_pdfs

def main():
    setup_logging()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default="test_data")
    args = parser.parse_args()
    print(ingest_pdfs(args.input_dir))

if __name__ == "__main__":
    main()