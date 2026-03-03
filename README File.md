# 📄 RAG Smart Contract Assistant

**Local Ollama + LangChain + Chroma + Gradio**

---

## 🚀 Project Overview

RAG Smart Contract Assistant is a fully modular **Retrieval-Augmented Generation (RAG)** system designed to analyze and query smart contracts and legal documents locally.

It is built using:

* **LangChain** – Orchestration Layer
* **Ollama (Local LLM)** – Qwen 3B
* **ChromaDB** – Local Persistent Vector Database
* **Gradio** – Interactive Web UI
* **Recursive Chunking + Local Embeddings**
* **Conversation Memory + Summarization**
* **Evaluation Pipeline**

### 🎯 Capabilities

The system allows users to:

1. Upload or ingest PDF contracts
2. Automatically extract, chunk, and embed documents
3. Perform semantic retrieval using vector search
4. Ask natural language questions
5. Receive grounded answers with inline citations
6. Maintain conversational memory
7. Evaluate response quality

---

# 🧠 System Architecture

## End-to-End Flow

```
User Question
      ↓
Retriever (ChromaDB)
      ↓
Top-K Relevant Chunks
      ↓
Prompt + Context Injection
      ↓
Local LLM (Qwen 3B - Ollama)
      ↓
Grounded Answer + Citations
```

---

# 🏗 Project Structure

```
rag-smart-contract-assistant/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── test_data/                 # Place PDFs here
│
├── data/
│   └── chroma/                # Auto-created persistent vector DB
│
├── src/
│   ├── rag_assistant/
│   │   ├── settings.py
│   │   ├── logging_config.py
│   │   ├── utils.py
│   │   │
│   │   ├── ingestion/
│   │   ├── vectorstore/
│   │   ├── llm/
│   │   ├── rag/
│   │   ├── ui/
│   │   ├── evaluation/
│   │
│   └── scripts/
│       ├── ingest_cli.py
│       ├── chat_cli.py
│       ├── run_gradio.py
│       └── run_eval.py
│
└── tests/
```

---

# ⚙️ Technologies Used

| Component     | Tool                     |
| ------------- | ------------------------ |
| LLM           | Qwen 3B via Ollama       |
| Embeddings    | nomic-embed-text (local) |
| Orchestration | LangChain                |
| Vector Store  | ChromaDB                 |
| UI            | Gradio                   |
| Evaluation    | RapidFuzz                |
| Language      | Python 3.10+             |

---

# 🔧 Installation Guide

## 1️⃣ Install Ollama

Download from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

## 2️⃣ Pull Required Models

```bash
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

Expected models:

* qwen2.5:3b
* nomic-embed-text

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Add PDF Documents

Place contracts inside:

```
test_data/
```

Example:

```
test_data/
 ├── Non-Disclosure-Agreement-Template.pdf
 ├── Business-Plan-Non-Disclosure-Agreement.pdf
```

---

# ▶️ Running the Project

## 🟢 Step 1 — Set Python Path (Windows PowerShell)

```powershell
$env:PYTHONPATH="src"
```

---

## 🟢 Step 2 — Ingest PDFs

```powershell
python -m scripts.ingest_cli --input_dir test_data
```

Expected output:

```
ok: True
pdf_count: X
chunk_count: X
persist_dir: data/chroma
```

---

## 🟢 Step 3 — Run Web UI

```powershell
python -m scripts.run_gradio
```

Open in browser:

```
http://localhost:7860
```

---

# 💬 CLI Mode (Optional)

Interactive terminal mode:

```powershell
python -m scripts.chat_cli
```

---

# 📊 Evaluation Mode

Edit:

```
src/rag_assistant/evaluation/goldens.json
```

Then run:

```powershell
python -m scripts.run_eval
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 🧩 Features

## ✅ Grounded Responses

Answers are strictly generated from retrieved document context.

## ✅ Inline Citations

Responses include references such as:

```
[Non-Disclosure-Agreement-Template.pdf:2]
```

## ✅ Conversation Memory

Maintains summarized dialogue state across multiple turns.

## ✅ Persistent Vector Store

Embeddings are stored locally in:

```
data/chroma/
```

## ✅ Modular Architecture

Each system component is isolated:

* Ingestion
* Retrieval
* LLM
* UI
* Evaluation

---

# 🛑 Hallucination Control

The system prompt enforces:

* Answer ONLY using retrieved context
* If answer is not found:

  ```
  I don't know based on the provided document.
  ```

---

# 🧠 Example Test Questions

* Who are the parties?
* What is the governing law?
* What is considered confidential information?
* What is the termination clause?
* How long does confidentiality last?

---

# ⚡ Troubleshooting

### Ollama not responding

```bash
ollama serve
```

### Model not found

```bash
ollama list
```

### Reset Vector Database

Delete:

```
data/chroma/
```

Then re-run ingestion.

---

# 📌 Demo Flow (For Presentation)

1. Show project structure
2. Ingest documents
3. Ask factual questions
4. Demonstrate citations
5. Ask out-of-scope question
6. Show hallucination prevention
7. Display evaluation metrics

---

# 🔒 Privacy

* Fully local execution
* No external API calls
* No cloud LLM usage
* No Docker required

---

# 👨‍💻 Author

**Mohammad Talal Omran**

---

**Fully Offline • Fully Modular • Fully Grounded**
