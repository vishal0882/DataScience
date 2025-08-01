# Insurance Policy RAG Agent

A Retrieval-Augmented Generation (RAG) agent built with Autogen to intelligently answer questions about insurance policies from a corpus of PDF documents.

## Project Structure

- `pdfs/`: Place your raw PDF files here.
- `src/`: Contains the core Python source code.
- `scripts/`: Standalone scripts for project setup.
- `main.py`: The entry point for the agent chat.
- `requirements.txt`: Project dependencies.
- `Dockerfile`: Instructions for building the application container.

## Getting Started

### 1. Setup

1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Place your PDF files** into the `pdfs/` directory.

### 2. Indexing Documents

Before you can ask questions, you must index your documents to build the vector database. Run the indexer script:

```bash
python scripts/run_indexer.py