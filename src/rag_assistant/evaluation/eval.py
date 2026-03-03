from __future__ import annotations
import json
from dataclasses import dataclass
from rapidfuzz import fuzz

from rag_assistant.rag.chain import build_rag_chain

@dataclass
class EvalResult:
    question: str
    score: int
    passed: bool
    answer_preview: str

def run_eval(goldens_path: str) -> dict:
    with open(goldens_path, "r", encoding="utf-8") as f:
        goldens = json.load(f)

    chain = build_rag_chain()
    results: list[EvalResult] = []

    for g in goldens:
        q = g["question"]
        expected = g.get("expected_contains", [])
        out = chain.invoke({"question": q, "summary": ""})
        ans = out["answer"]

        ans_l = ans.lower()
        passed = any(e.lower() in ans_l for e in expected) if expected else True

        joined = " ".join(expected)
        score = fuzz.partial_ratio(joined.lower(), ans_l) if joined else 100
        results.append(EvalResult(q, score, passed, ans[:220].replace("\n", " ")))

    return {
        "total": len(results),
        "passed": sum(1 for r in results if r.passed),
        "avg_score": round(sum(r.score for r in results) / max(1, len(results)), 2),
        "details": [r.__dict__ for r in results],
    }