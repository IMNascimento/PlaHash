import PyPDF2
from .document_reader import DocumentReader

class PDFReader(DocumentReader):
    def read(self, file_path):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfFileReader(file)
            return " ".join(reader.getPage(i).extract_text() for i in range(reader.numPages))