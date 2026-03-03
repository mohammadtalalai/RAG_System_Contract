from __future__ import annotations
from rag_assistant.evaluation.eval import run_eval

def main():
    print(run_eval("src/rag_assistant/evaluation/goldens.json"))

if __name__ == "__main__":
    main()