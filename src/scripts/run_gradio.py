from __future__ import annotations
from rag_assistant.ui.gradio_app import build_app

def main():
    app = build_app()
    app.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()