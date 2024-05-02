import pytest
from readers.docx_reader import DocxReader
from readers.pdf_reader import PDFReader
from readers.odt_reader import ODTReader
from readers.html_reader import HTMLReader
from readers.txt_reader import TXTReader

def test_docx_reader():
    reader = DocxReader()
    # Suponha que você tem um arquivo de teste específico para isso
    # Este teste é meramente ilustrativo, ajuste conforme a necessidade
    content = reader.read('tests/test_files/example.docx')
    assert 'Hello World' in content, "DocxReader failed to read the DOCX file correctly."

def test_pdf_reader():
    reader = PDFReader()
    content = reader.read('tests/test_files/example.pdf')
    assert 'Hello World' in content, "PDFReader failed to read the PDF file correctly."

def test_odt_reader():
    reader = ODTReader()
    content = reader.read('tests/test_files/example.odt')
    assert 'Hello World' in content, "ODTReader failed to read the ODT file correctly."

def test_html_reader():
    reader = HTMLReader()
    content = reader.read('tests/test_files/example.html')
    assert 'Hello World' in content, "HTMLReader failed to read the HTML file correctly."

def test_txt_reader():
    reader = TXTReader()
    content = reader.read('tests/test_files/example.txt')
    assert 'Hello World' in content, "TXTReader failed to read the TXT file correctly."