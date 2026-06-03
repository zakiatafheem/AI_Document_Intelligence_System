"""
This file is responsible for:
1. Loading PDF documents
2. Splitting documents into chunks
"""

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(pdf_path):
    """
    Load PDF and return pages
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents


def split_documents(documents):
    """
    Split PDF pages into smaller chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    return chunks