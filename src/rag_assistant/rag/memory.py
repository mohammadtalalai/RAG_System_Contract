from __future__ import annotations
from dataclasses import dataclass

@dataclass
class DialogState:
    summary: str = ""

def update_summary(llm, old_summary: str, user_msg: str, assistant_msg: str) -> str:
    prompt = (
        "You are a summarizer. Keep a short running summary of the conversation.\n"
        "Update the summary using the latest exchange.\n\n"
        f"Old summary:\n{old_summary}\n\n"
        f"User:\n{user_msg}\n\n"
        f"Assistant:\n{assistant_msg}\n\n"
        "New summary (2-6 bullet points max, concise):"
    )
    resp = llm.invoke(prompt)
    return getattr(resp, "content", str(resp)).strip()