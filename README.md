# ⚡ Resume Chatbot (RAG with Groq & Llama 3.1)

A fast, contextual **Retrieval-Augmented Generation (RAG)** chatbot built to provide instant, accurate answers from the Tekdex HR Policy Document.

The application leverages **Groq's LPU** for lightning-fast inference and **LangChain's Conversational Chain** for memory and context awareness.

---

## ✨ Key Features

* **⚡ Groq Speed:** Utilizes the `llama-3.1-8b-instant` model on Groq for sub-second, real-time responses.
* **🧠 Conversational Memory:** Implemented with **`ConversationBufferMemory`** to maintain context and handle follow-up questions naturally.
* **🔍 Accurate RAG:** Answers are strictly grounded in the **Provided Resume**, minimizing hallucinations.
* **💾 Local Vector Store:** Uses **ChromaDB** with **`all-MiniLM-L6-v2`** embeddings for efficient semantic search.

---

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **LLM** | `llama-3.1-8b-instant` (via Groq) | Fast, High-Quality Answer Generation |
| **Framework** | LangChain | Orchestration & RAG Pipeline |
| **Vector DB** | ChromaDB | Document Indexing & Retrieval |
| **Embeddings** | `all-MiniLM-L6-v2` | Semantic Search Encoding |

---

## 🚀 Getting Started

### 1. Installation

# Clone the repository
git clone <your-repo-link>
cd rag

# Install dependencies
pip install -r requirements.txt

# API Key Setup
 .env file
GROQ_API_KEY="sk_..."

# Data Preparation
python data_prep.py

# Run The Chatbot
python app.py
