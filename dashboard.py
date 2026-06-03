# dashboard.py

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QVBoxLayout
)

from pdf_loader import load_pdf, split_documents
from rag import create_vector_store, ask_document


class DocumentAI(QWidget):

    def __init__(self):
        super().__init__()

        self.vector_store = None

        self.setWindowTitle("AI PDF Assistant")
        self.resize(600, 400)

        layout = QVBoxLayout()

        self.upload_btn = QPushButton("Upload PDF")
        self.upload_btn.clicked.connect(self.upload_pdf)

        self.question_box = QTextEdit()

        self.ask_btn = QPushButton("Ask")
        self.ask_btn.clicked.connect(self.ask_question)

        self.answer_box = QTextEdit()
        self.answer_box.setReadOnly(True)

        layout.addWidget(self.upload_btn)
        layout.addWidget(self.question_box)
        layout.addWidget(self.ask_btn)
        layout.addWidget(self.answer_box)

        self.setLayout(layout)

    def upload_pdf(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF",
            "",
            "PDF Files (*.pdf)"
        )

        if file_path:

            docs = load_pdf(file_path)

            chunks = split_documents(docs)

            self.vector_store = create_vector_store(chunks)

            self.answer_box.setText("PDF Loaded Successfully!")

    def ask_question(self):

        if self.vector_store is None:
            self.answer_box.setText("Upload PDF First")
            return

        question = self.question_box.toPlainText()

        answer = ask_document(
            question,
            self.vector_store
        )

        self.answer_box.setText(answer)


def run_app():

    app = QApplication(sys.argv)

    window = DocumentAI()

    window.show()

    sys.exit(app.exec_())