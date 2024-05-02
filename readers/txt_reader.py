from .document_reader import DocumentReader

class TXTReader(DocumentReader):
    def read(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()