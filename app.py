import streamlit as st
from pathlib import Path

from src.rag_pipline import create_rag_pipeline, answer_question
from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# RAG PIPELINE
# ============================================================

@st.cache_resource
def load_rag_pipeline(file_name):
    return create_rag_pipeline(file_name)


# ============================================================
# APPLICATION HEADER
# ============================================================

st.title("📚 RAG Document Q&A Assistant")

st.write(
    "Ask questions about the documents stored in the knowledge base."
)


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

st.sidebar.header("📤 Upload Documents")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


# ============================================================
# DOCUMENT SCOPE
# ============================================================

documents_path = Path("data/documents")

pdf_files = sorted(
    documents_path.glob("*.pdf")
)

pdf_names = [
    pdf.name
    for pdf in pdf_files
]

selected_document = None

if pdf_names:

    document_scope = st.sidebar.radio(
        "📄 Document Scope",
        [
            "All Documents",
            "Select a Document"
        ]
    )

    if document_scope == "Select a Document":

        selected_document = st.sidebar.selectbox(
            "Choose Document",
            pdf_names
        )


# ============================================================
# PROCESS UPLOADED DOCUMENT
# ============================================================

if uploaded_file is not None:

    documents_path.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = documents_path / uploaded_file.name

    if file_path.exists():

        st.sidebar.warning(
            f"⚠️ `{uploaded_file.name}` already exists."
        )

    else:

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.sidebar.success(
            f"✅ Uploaded: {uploaded_file.name}"
        )

    if st.sidebar.button("🔄 Process Document"):

        with st.spinner("Processing document..."):

            try:

                documents = load_documents()

                chunks = split_documents(
                    documents
                )

                embeddings = create_embeddings()

                create_vector_store(
                    chunks,
                    embeddings
                )

                st.cache_resource.clear()

                st.sidebar.success(
                    "✅ Document processed successfully!"
                )

                st.rerun()

            except FileNotFoundError:

                st.sidebar.error(
                    "❌ No PDF documents were found."
                )

            except Exception:

                st.sidebar.error(
                    "❌ Failed to process the document. "
                    "Please check the PDF and try again."
                )


# ============================================================
# LOAD RAG SYSTEM
# ============================================================

try:

    retriever, prompt, llm = load_rag_pipeline(
        selected_document
    )

except FileNotFoundError:

    st.error(
        "❌ Knowledge base not found. "
        "Please upload and process a PDF document first."
    )

    st.stop()

except ValueError as e:

    st.error(
        f"❌ Configuration error: {e}"
    )

    st.stop()

except Exception:

    st.error(
        "❌ Failed to load the RAG system. "
        "Please check your configuration and try again."
    )

    st.stop()


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# QUESTION INPUT
# ============================================================

question = st.chat_input(
    "Ask a question about the documents..."
)

if question:

    question = question.strip()


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching documents and generating answer..."
        ):

            try:

                answer, source_documents = answer_question(
                    question,
                    retriever,
                    prompt,
                    llm
                )

                st.markdown(answer)

                # =================================================
                # RETRIEVED SOURCES
                # =================================================

                with st.expander(
                    "📚 View Retrieved Sources"
                ):

                    for index, document in enumerate(
                        source_documents,
                        start=1
                    ):

                        source = document.metadata.get(
                            "source",
                            "Unknown"
                        )

                        page = document.metadata.get(
                            "page",
                            "Unknown"
                        )

                        if isinstance(page, int):

                            page = page + 1

                        source_name = (
                            source
                            .replace("\\", "/")
                            .split("/")[-1]
                        )

                        st.markdown(
                            f"**Source {index}:** "
                            f"📄 `{source_name}`"
                        )

                        st.markdown(
                            f"**Page:** {page}"
                        )

                        st.caption(
                            document.page_content[:500]
                        )

                        if index < len(source_documents):

                            st.divider()

            except Exception:

                st.error(
                    "❌ Something went wrong while "
                    "processing your question. "
                    "Please try again."
                )

                answer = (
                    "Sorry, I could not process your question."
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )