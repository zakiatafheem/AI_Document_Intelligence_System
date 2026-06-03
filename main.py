from pdf_loader import load_pdf
from pdf_loader import split_documents

from rag import create_vector_store
from rag import ask_document

from dashboard import run_app

run_app()

# PDF path

pdf_path = "sample.pdf"

# Load PDF

documents = load_pdf(pdf_path)

# Split into chunks

chunks = split_documents(documents)

# Create vector database

vector_store = create_vector_store(chunks)

print("PDF Loaded Successfully!")

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    answer = ask_document(
        question,
        vector_store
    )

    print("\nAnswer:")
    print(answer)