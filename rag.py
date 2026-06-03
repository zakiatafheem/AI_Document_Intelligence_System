"""
This file contains:
1. Embedding creation
2. FAISS vector store
3. Retrieval
4. RAG pipeline
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from groq_client import ask_groq

# Create embedding model

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_store(chunks):
    """
    Create FAISS vector store
    """

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store


def ask_document(question, vector_store):
    """
    Perform retrieval
    Build context
    Send to Groq
    """

    retrieved_docs = vector_store.similarity_search(
        question,
        k=3
    )

    context = ""

    for doc in retrieved_docs:
        context += doc.page_content + "\n"

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    answer = ask_groq(prompt)

    return answer