from __future__ import annotations
import gradio as gr
import logging

from rag_assistant.logging_config import setup_logging
from rag_assistant.settings import settings
from rag_assistant.ingestion.ingest import ingest_pdfs
from rag_assistant.rag.chain import build_rag_chain
from rag_assistant.rag.memory import DialogState, update_summary
from rag_assistant.llm.models import get_chat_model

logger = logging.getLogger(__name__)

def build_app():
    setup_logging()

    rag_chain = build_rag_chain()
    summarizer_llm = get_chat_model(temperature=0.0)

    with gr.Blocks(title="RAG Smart Contract Assistant") as demo:
        # ✅ لازم State يتعمل جوّه Blocks
        state = gr.State(DialogState(summary=""))

        gr.Markdown("# 📄 RAG Smart Contract Assistant (Local Ollama + Chroma + Gradio)")
        gr.Markdown(
            f"- Put PDFs in `{settings.test_data_dir}` ثم اضغط **Ingest**.\n"
            f"- الإجابات grounded مع citations مثل `[file.pdf:3]`.\n"
            f"- Local model: `{settings.ollama_chat_model}` | embeddings: `{settings.ollama_embed_model}`"
        )

        with gr.Row():
            ingest_btn = gr.Button("Ingest test_data PDFs")
            ingest_out = gr.JSON()

        with gr.Row():
            upload = gr.File(label="Upload PDF (optional)", file_types=[".pdf"])
            upload_btn = gr.Button("Ingest Uploaded PDF")

        chatbot = gr.Chatbot(type="messages", height=420)
        msg = gr.Textbox(label="Ask a question", placeholder="مثال: ما هو نطاق العقد؟")
        send = gr.Button("Send")

        def do_ingest():
            return ingest_pdfs(settings.test_data_dir)

        def do_ingest_uploaded(file_obj):
            if file_obj is None:
                return {"ok": False, "message": "No file uploaded"}

            import shutil, os
            os.makedirs(settings.test_data_dir, exist_ok=True)
            dst = os.path.join(settings.test_data_dir, os.path.basename(file_obj.name))
            shutil.copy(file_obj.name, dst)
            return ingest_pdfs(settings.test_data_dir)

        def respond(user_message, history, st: DialogState):
            out = rag_chain.invoke({"question": user_message, "summary": st.summary})
            answer = out["answer"]

            try:
                st.summary = update_summary(summarizer_llm, st.summary, user_message, answer)
            except Exception as e:
                logger.warning("Summary update failed: %s", e)

            history = history + [
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": answer},
            ]
            return history, st

        ingest_btn.click(fn=do_ingest, inputs=None, outputs=ingest_out)
        upload_btn.click(fn=do_ingest_uploaded, inputs=upload, outputs=ingest_out)

        # مهم: inputs/outputs بنفس الترتيب
        send.click(fn=respond, inputs=[msg, chatbot, state], outputs=[chatbot, state])
        msg.submit(fn=respond, inputs=[msg, chatbot, state], outputs=[chatbot, state])

    return demo