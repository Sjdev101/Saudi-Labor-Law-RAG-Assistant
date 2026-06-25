# 🇸🇦 Saudi Labor Law RAG Assistant

> An AI-powered Retrieval-Augmented Generation (RAG) application that answers questions about the Saudi Labor Law using semantic search, vector embeddings, and a Large Language Model (LLM).

---

## Overview

The Saudi Labor Law RAG Assistant enables users to ask natural language questions about the Saudi Labor Law and receive answers grounded in the official document.

Instead of relying solely on the language model's knowledge, the system retrieves the most relevant sections of the Saudi Labor Law PDF from a vector database before generating a response. This Retrieval-Augmented Generation (RAG) approach improves factual accuracy and reduces hallucinations.

---

## Features

* PDF text extraction
* Automatic document chunking
* Semantic search using embeddings
* ChromaDB vector database
* AI-generated answers using retrieved context
* Secure API key management using environment variables
* Modular Python implementation
* Easily extendable architecture

---

# System Architecture

```text
                    Saudi Labor Law PDF
                             │
                             ▼
                  PDF Text Extraction
                         (PyPDF)
                             │
                             ▼
                     Document Chunking
                             │
                             ▼
                  Embedding Generation
               (Sentence Transformers)
                             │
                             ▼
                 ChromaDB Vector Store
                             │
                             ▼
                     Similarity Search
                             │
                             ▼
                  Top Relevant Chunks
                             │
                             ▼
                    Large Language Model
                     (OpenAI / Grok API)
                             │
                             ▼
                  Grounded AI Response
```

---

# Tech Stack

| Category              | Technology             |
| --------------------- | ---------------------- |
| Language              | Python 3               |
| PDF Parser            | PyPDF                  |
| Embeddings            | Sentence Transformers  |
| Embedding Model       | BAAI/bge-small-en-v1.5 |
| Vector Database       | ChromaDB               |
| LLM                   | OpenAI API or Grok API |
| Environment Variables | python-dotenv          |
| Version Control       | Git & GitHub           |

---

# Project Structure

```text
saudi-labor-law-rag/
│
├── data/
│   └── labor_law.pdf
│
├── chroma_db/
│
├── ingest.py
├── query.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/saudi-labor-law-rag.git

cd saudi-labor-law-rag
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the project root.

## OpenAI

```env
OPENAI_API_KEY=your_openai_api_key
```

or

## Grok (xAI)

```env
XAI_API_KEY=your_xai_api_key
```

---

# Building the Knowledge Base

Place the Saudi Labor Law PDF inside the `data/` directory.

Run:

```bash
python ingest.py
```

This process:

* Reads the PDF
* Extracts text
* Splits the document into chunks
* Generates embeddings
* Stores embeddings in ChromaDB

---

# Running the Application

```bash
python query.py
```

Example questions:

* How many annual leave days does an employee receive?
* What is the probation period?
* How is overtime calculated?
* What are the rules regarding termination?
* What are an employer's obligations?

---

# How It Works

1. User submits a question.
2. The question is converted into a vector embedding.
3. ChromaDB performs semantic similarity search.
4. The most relevant document chunks are retrieved.
5. Retrieved context is passed to the language model.
6. The model generates a response using only the retrieved information.

---

# Example Workflow

```text
User Question
      │
      ▼
Embedding Model
      │
      ▼
ChromaDB Similarity Search
      │
      ▼
Top Matching Chunks
      │
      ▼
LLM Prompt
      │
      ▼
Grounded Answer
```

---

# Current Features

* ✅ PDF ingestion
* ✅ Text chunking
* ✅ Semantic embeddings
* ✅ Vector database
* ✅ Retrieval pipeline
* ✅ AI-generated answers
* ✅ Environment variable support

---

# Future Improvements

* Article-aware chunking
* Source citations (Article and page number)
* Arabic language support
* Hybrid search (BM25 + Vector Search)
* FastAPI REST API
* Streamlit or React frontend
* Docker deployment
* Evaluation dataset
* Unit tests
* Conversation memory
* Response streaming
* Reranking for improved retrieval accuracy

---

# Disclaimer

This project is intended for educational and portfolio purposes only.

The generated responses should not be considered legal advice. Users should always verify information against the official Saudi Labor Law and consult qualified legal professionals where appropriate.

---

# License

This project is licensed under the MIT License.

---

# Author

**Sohaib Abbasi**

* Electrical Engineering Graduate (NUST)
* AI & Machine Learning Enthusiast
* Interested in Retrieval-Augmented Generation (RAG), NLP, and AI Systems

GitHub: https://github.com/YOUR_GITHUB_USERNAME

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
