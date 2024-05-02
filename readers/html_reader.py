from .document_reader import DocumentReader
from bs4 import BeautifulSoup

class HTMLReader(DocumentReader):
    def read(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, "html.parser")
            return soup.get_text()