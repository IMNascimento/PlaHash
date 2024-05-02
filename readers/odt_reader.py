from .document_reader import DocumentReader
from odf import text, teletype
from odf.opendocument import load as load_odf

class ODTReader(DocumentReader):
    def read(self, file_path):
        doc = load_odf(file_path)
        all_texts = teletype.extractText(doc.text)  
        return all_texts