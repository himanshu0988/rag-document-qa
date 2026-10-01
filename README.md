# 📚 RAG Document Q&A Assistant

A Retrieval-Augmented Generation (RAG) based document question-answering assistant built with Python, LangChain, OpenAI, FAISS, and Streamlit.

The application allows users to upload PDF documents, process them into a searchable vector database, and ask natural-language questions about the uploaded documents.

---

## 🚀 Features

- 📄 Upload PDF documents
- 📚 Support multiple PDF documents
- ✂️ Split documents into smaller chunks
- 🧠 Generate embeddings using OpenAI
- 🔎 Semantic document retrieval using FAISS
- 🤖 Generate answers using an OpenAI LLM
- 📌 Display retrieved document sources
- 📑 Display source page numbers
- 💬 Interactive Streamlit chat interface
- 🛡️ Grounded responses using retrieved document context
- ⚠️ Clean error handling
- 🔄 Rebuild the vector store when documents are processed
- 🚫 Detect duplicate PDF uploads

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │  PDF Documents  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ PDF Document    │
                    │ Loader          │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Text Splitter  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ OpenAI          │
                    │ Embeddings      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ FAISS Vector    │
                    │ Store           │
                    └────────┬────────┘
                             │
                             │
User Question ───────────────┤
                             ▼
                    ┌─────────────────┐
                    │    Retriever    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Retrieved       │
                    │ Context         │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   LLM + Prompt  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Answer      │

                    
## 📁 Project Structure           

rag-document-qa/
│
├── data/
│   └── documents/
│       ├── python_guide.pdf
│       ├── machine_learning_guide.pdf
│       └── ...
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
├── README.md
├── requirements.txt
└── .gitignore   └─────────────────┘

⚙️ Installation
1. Clone the repository
git clone <your-github-repository-url>
cd rag-document-qa
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
Windows PowerShell
.\.venv\Scripts\Activate.ps1

If PowerShell does not allow activation, run:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then activate again:

.\.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key

The .env file contains the API key and should never be uploaded to GitHub.

The project uses python-dotenv to load the API key from the .env file.

📄 Documents

Place PDF documents inside:

data/documents/

Example:

data/
└── documents/
    ├── python_guide.pdf
    ├── machine_learning_guide.pdf
    └── deep_learning_guide.pdf

The application supports multiple PDF documents.

Documents can also be uploaded directly through the Streamlit sidebar.

🗂️ Vector Store

The project uses FAISS as the vector database.

During document processing:

PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embeddings
 ↓
FAISS Vector Store

The FAISS index is stored locally in:

vectorstore/faiss_index/

The vector store is generated automatically when documents are processed.

The vectorstore/ directory is excluded from GitHub using .gitignore.

▶️ Running the Application
1. Activate the virtual environment
.\.venv\Scripts\Activate.ps1
2. Process the documents
python ingest.py

This creates the FAISS vector store from the PDFs.

3. Start the Streamlit application
streamlit run app.py

The application will open in your browser.

You can then:

Upload a PDF document.
Click Process Document.
Ask questions about the documents.
View the retrieved sources and page numbers.
❓ Example Questions

You can ask questions such as:

What is a Python list?
What is supervised learning?
What is the difference between classification and regression?
What is deep learning?
What are neural networks?
What is the purpose of feature engineering?
What is NLP?
What are the advantages of machine learning?

The assistant answers questions using information retrieved from the uploaded documents.

🧠 How RAG Works

This project uses Retrieval-Augmented Generation (RAG).

The complete workflow is:

PDF Documents
      ↓
Document Loader
      ↓
Text Splitter
      ↓
OpenAI Embeddings
      ↓
FAISS Vector Store

User Question
      ↓
Retriever
      ↓
Relevant Document Chunks
      ↓
Prompt + Retrieved Context
      ↓
LLM
      ↓
Answer
Step 1 — Document Loading

PDF documents are loaded using PyPDFLoader.

Step 2 — Text Splitting

Large documents are divided into smaller chunks using a recursive text splitter.

Step 3 — Embeddings

Each text chunk is converted into a numerical vector using OpenAI embeddings.

Step 4 — Vector Storage

The embeddings are stored in a FAISS vector store.

Step 5 — Retrieval

When the user asks a question, the system searches FAISS for the most relevant document chunks.

Step 6 — Generation

The retrieved context is provided to the LLM along with the user's question.

Step 7 — Answer

The LLM generates an answer based on the retrieved document context.

This helps the application provide answers grounded in the uploaded documents rather than relying only on the model's general knowledge.

🚀 Future Improvements

Possible future improvements include:

Support for additional document formats such as DOCX and TXT
Improved document management
Conversation memory
Streaming responses
Better source citations
Authentication and user accounts
Cloud-based vector databases
Advanced retrieval techniques
Reranking retrieved documents
Support for additional LLM providers
Deployment to a cloud platform
Improved user interface
Document deletion and management
Multi-user document collections
🎯 Project Goal

The goal of this project is to build a practical Retrieval-Augmented Generation (RAG) application that can answer questions from custom documents.

The project demonstrates practical experience with:

Python
LangChain
Large Language Models
Generative AI
Embeddings
FAISS
Natural Language Processing
Document processing
Information retrieval
Streamlit
Prompt engineering
API integration
👨‍💻 Author

Himanshu Kumar Singh

Aspiring AI Engineer | LLM / GenAI Enthusiast

Technologies Used

Python • LangChain • OpenAI • FAISS • Streamlit • NLP • Generative AI