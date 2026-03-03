from pydantic import BaseModel

class Settings(BaseModel):
    # ===== Local LLM (Ollama) =====
    ollama_base_url: str = "http://localhost:11434"
    ollama_chat_model: str = "qwen2.5:3b"          # غيره حسب اللي عندك
    ollama_embed_model: str = "nomic-embed-text" # embeddings محلية ممتازة

    # ===== Paths =====
    chroma_dir: str = "data/chroma"
    test_data_dir: str = "test_data"

    # ===== Chunking =====
    chunk_size: int = 1000
    chunk_overlap: int = 150

    # ===== Retrieval =====
    top_k: int = 5

settings = Settings()