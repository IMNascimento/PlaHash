from docx import Document
from .document_reader import DocumentReader

class DocxReader(DocumentReader):
    def read(self, file_path):
        doc = Document(file_path)
        return " ".join(para.text for para in doc.paragraphs)