from __future__ import annotations
from rag_assistant.logging_config import setup_logging
from rag_assistant.rag.chain import build_rag_chain
from rag_assistant.rag.memory import DialogState, update_summary
from rag_assistant.llm.models import get_chat_model

def main():
    setup_logging()
    chain = build_rag_chain()
    summarizer = get_chat_model(temperature=0.0)
    st = DialogState(summary="")

    print("RAG CLI (local). Type 'exit' to quit.\n")
    while True:
        q = input("You> ").strip()
        if q.lower() in {"exit", "quit"}:
            break
        out = chain.invoke({"question": q, "summary": st.summary})
        ans = out["answer"]
        print(f"\nAssistant>\n{ans}\n")
        try:
            st.summary = update_summary(summarizer, st.summary, q, ans)
        except Exception:
            pass

if __name__ == "__main__":
    main()