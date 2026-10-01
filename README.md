# 📚 RAG Document Q&A Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about PDF documents and receive grounded answers using retrieved document context.

Built with **Python, LangChain, OpenAI, FAISS, and Streamlit**.

---

## 🚀 Features

* 📄 Upload PDF documents through the Streamlit interface
* 📚 Support multiple PDF documents
* 🔍 Semantic search using vector embeddings
* 🧠 OpenAI embeddings for document representation
* ⚡ FAISS vector store for fast similarity search
* 🤖 OpenAI LLM for answer generation
* 🎯 Top-K relevant document chunk retrieval
* 🔎 Search across all documents
* 📑 Option to restrict retrieval to a specific document
* 📄 Display retrieved source documents and page numbers
* 🛡️ Grounded responses using retrieved document context
* 💬 Interactive Streamlit chat interface
* ⚠️ Handles missing documents and configuration errors
* 🔄 Rebuilds the vector store when documents are processed

---

## 🏗️ Architecture

```text
                    PDF Documents
                          │
                          ▼
                  PDF Document Loader
                          │
                          ▼
                    Text Splitter
                          │
                          ▼
                   OpenAI Embeddings
                          │
                          ▼
                    FAISS Vector Store
                          │
                          │
                    User Question
                          │
                          ▼
                       Retriever
                          │
                          ▼
                 Retrieved Context
                          │
                          ▼
                  Prompt + OpenAI LLM
                          │
                          ▼
                        Answer
```

---

## 📁 Project Structure

```text
rag-document-qa/
│
├── data/
│   └── documents/
│       └── PDF documents
│
├── vectorstore/
│   └── faiss_index/
│
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── prompt.py
│   ├── rag_pipline.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
├── app.py
├── ingest.py
├── requirements.txt
├── .gitignore
└── README.md
```

> `.env`, uploaded PDFs, and the generated FAISS vector store are excluded from Git using `.gitignore`.

---

## 🛠️ Technologies Used

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Application development         |
| LangChain     | RAG pipeline components         |
| OpenAI        | Embeddings and LLM              |
| FAISS         | Vector similarity search        |
| PyPDF         | PDF document loading            |
| Streamlit     | Web application interface       |
| python-dotenv | Environment variable management |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/himanshu0988/rag-document-qa.git
```

```bash
cd rag-document-qa
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openai_api_key
```

Example project structure:

```text
rag-document-qa/
├── .env
├── app.py
├── ingest.py
└── ...
```

**Never commit your `.env` file or API key to GitHub.**

---

## 📄 Adding Documents

PDF documents can be uploaded directly through the Streamlit sidebar.

The application stores uploaded PDFs in:

```text
data/documents/
```

The application supports two retrieval modes:

### All Documents

Searches across all PDFs in the knowledge base.

### Select a Document

Restricts retrieval to the selected PDF using document metadata.

---

## 🗄️ Vector Store

The application uses **FAISS** to store document embeddings.

The vector store is generated at:

```text
vectorstore/faiss_index/
```

It is intentionally excluded from GitHub because it is a generated artifact.

To rebuild the vector store manually:

```powershell
python ingest.py
```

The ingestion pipeline performs:

```text
PDFs
 ↓
Document Loading
 ↓
Text Chunking
 ↓
OpenAI Embeddings
 ↓
FAISS Vector Store
```

---

## ▶️ Running the Application

Start Streamlit:

```powershell
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 💬 Example Questions

Depending on the documents uploaded, example questions could include:

```text
What are the main features of Python?
```

```text
How are machine learning and deep learning different?
```

```text
What concepts are discussed in this document?
```

You can also select a specific document and ask questions about that document only.

---

## 🧠 How RAG Works

### 1. Document Loading

PDF documents are loaded using `PyPDFLoader`.

### 2. Text Chunking

Large documents are divided into smaller chunks using `RecursiveCharacterTextSplitter`.

The current configuration uses:

```text
Chunk Size: 1500
Chunk Overlap: 300
```

### 3. Embeddings

Each document chunk is converted into a numerical vector using:

```text
text-embedding-3-small
```

### 4. Vector Storage

The generated vectors are stored in a FAISS vector database.

### 5. Retrieval

When a user asks a question, the system performs similarity search and retrieves the most relevant chunks.

The current configuration retrieves:

```text
Top-K = 6
```

### 6. Context Construction

The retrieved chunks are combined into a context passed to the LLM.

### 7. Prompting

The prompt instructs the LLM to answer using only the retrieved context.

### 8. Answer Generation

The OpenAI LLM generates the final answer using the retrieved document information.

```text
User Question
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
Retrieved Context
      ↓
Prompt
      ↓
OpenAI LLM
      ↓
Grounded Answer
```

---

## 🛡️ Grounding and Hallucination Control

The application uses a prompt that instructs the model to:

* Use only retrieved document context
* Avoid using outside information
* Avoid inventing information
* Clearly indicate when the answer cannot be found in the documents

When the retrieved context does not contain enough information, the application returns:

```text
I could not find the answer in the provided documents.
```

---

## 🔎 Source Retrieval

For each answer, the application provides a **View Retrieved Sources** section.

It displays:

* Source document name
* Page number
* Retrieved text preview

This helps users understand which document content was used to generate the answer.

---

## 🔮 Future Improvements

Possible future improvements include:

* Reranking retrieved documents
* Metadata-based filtering by additional fields
* Conversation-aware retrieval
* Streaming LLM responses
* Authentication and user management
* Support for additional document formats
* Improved retrieval strategies
* Production deployment
* Monitoring and logging
* Automated RAG evaluation

---

## 🎯 Project Goal

The goal of this project is to demonstrate an end-to-end **Retrieval-Augmented Generation pipeline** that combines document processing, semantic retrieval, vector search, prompt engineering, and LLM-based answer generation.

The project is designed to provide answers grounded in a user's own document collection rather than relying only on the model's general knowledge.

---

## 👨‍💻 Author

**Himanshu Kumar Singh**

---

## ⭐ Technologies

**Python • LangChain • OpenAI • FAISS • Streamlit • PyPDF**
