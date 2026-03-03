from __future__ import annotations
import os

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def list_pdfs(input_dir: str) -> list[str]:
    files: list[str] = []
    for root, _, names in os.walk(input_dir):
        for n in names:
            if n.lower().endswith(".pdf"):
                files.append(os.path.join(root, n))
    return sorted(files)

def safe_filename(path: str) -> str:
    return os.path.basename(path)