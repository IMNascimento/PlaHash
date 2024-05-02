from PyPDF2 import PdfReader
from .document_reader import DocumentReader

class PDFReader(DocumentReader):
    def read(self, file_path):
        with open(file_path, "rb") as file:
            reader = PdfReader(file)
            return " ".join(page.extract_text() for page in reader.pages)