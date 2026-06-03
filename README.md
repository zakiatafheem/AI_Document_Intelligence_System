# AI Document Intelligence System

## Overview

AI Document Intelligence System is a desktop-based application that allows users to upload PDF documents and ask natural language questions about their content. The system uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information from the uploaded document and generate accurate responses using Groq LLM.

This project demonstrates the integration of Generative AI, Vector Databases, Document Processing, and Desktop Application Development using Python.

---

# Problem Statement

Organizations often store important information in large PDF documents such as policies, manuals, reports, and documentation. Manually searching through these documents to find specific information is time-consuming and inefficient.

There is a need for an intelligent system that can understand document content and answer user questions quickly and accurately.

---

# Objective

The objective of this project is to build an AI-powered document assistant that:

- Accepts PDF documents as input
- Processes and understands document content
- Retrieves relevant information using semantic search
- Answers user questions in natural language
- Provides a simple desktop-based user interface

---

# Features

- Upload PDF Documents
- Automatic Document Chunking
- Embedding Generation
- Vector Similarity Search using FAISS
- Question Answering using Groq LLM
- User-Friendly PyQt5 Interface
- Real-Time Responses from Uploaded Documents

---

# System Workflow

1. User uploads a PDF document.
2. PDF content is extracted.
3. Text is divided into smaller chunks.
4. Embeddings are generated for each chunk.
5. Embeddings are stored in FAISS vector database.
6. User enters a question.
7. Relevant chunks are retrieved using similarity search.
8. Retrieved context is sent to Groq LLM.
9. AI-generated answer is displayed to the user.

---

# Tech Stack

## Programming Language

- Python

## AI / GenAI

- Groq API
- Llama 3.3 70B Versatile

## RAG Components

- LangChain
- FAISS
- HuggingFace Embeddings

## Document Processing

- PyPDF

## GUI

- PyQt5

---

# Project Structure

```text
AI_Document_Intelligence/

├── main.py
├── dashboard.py
├── pdf_loader.py
├── rag.py
├── groq_client.py
├── requirements.txt
├── README.md
├── .env (should consist of api key)
└── sample.pdf
```

---

# File Description

## main.py

Entry point of the application.

Responsibilities:
- Starts the PyQt5 application
- Launches the main window

---

## dashboard.py

Graphical User Interface.

Responsibilities:
- PDF Upload
- User Question Input
- Display Answers
- User Interaction

---

## pdf_loader.py

PDF processing module.

Responsibilities:
- Load PDF documents
- Extract text
- Split text into chunks

---

## rag.py

Core RAG implementation.

Responsibilities:
- Create embeddings
- Build FAISS vector store
- Retrieve relevant chunks
- Generate contextual responses

---

## groq_client.py

Groq API integration.

Responsibilities:
- Connect to Groq LLM
- Send prompts
- Receive responses

---

# Challenges Faced

### 1. Context Retrieval

Ensuring only relevant document chunks are retrieved before sending context to the LLM.

### 2. API Integration

Integrating Groq API and handling responses efficiently.

### 3. Desktop Application Development

Connecting AI backend components with the PyQt5 user interface.

---

# Outcomes

- Successfully built an AI-powered desktop application.
- Implemented Retrieval-Augmented Generation (RAG) pipeline.
- Improved document search and information retrieval process.
- Demonstrated practical usage of Vector Databases and LLM integration.
- Gained hands-on experience with modern Generative AI technologies.

---

# Learning Outcomes

Through this project, I gained experience in:

- Desktop Application Development using PyQt5
- Generative AI Applications
- Retrieval-Augmented Generation (RAG)
- Vector Databases (FAISS)
- Embeddings and Semantic Search
- LangChain Framework
- Groq LLM Integration


---

# Future Enhancements

- Multiple PDF Support
- Chat History Management
- Source Citation Display
- Document Summarization
- Support for DOCX and TXT Files
- Export Responses to PDF
- Multi-Document Search

---

