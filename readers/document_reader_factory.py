from .document_reader import DocumentReader
from .docx_reader import DocxReader
from .pdf_reader import PDFReader
from .odt_reader import ODTReader
from .html_reader import HTMLReader
from .txt_reader import TXTReader

class DocumentReaderFactory:
    """
    Factory class to create document reader instances based on file type.
    """
    @staticmethod
    def get_reader(file_type):
        readers = {
            "docx": DocxReader,
            "pdf": PDFReader,
            "odt": ODTReader,
            "html": HTMLReader,
            "txt": TXTReader
        }
        reader_class = readers.get(file_type)
        return reader_class() if reader_class else None