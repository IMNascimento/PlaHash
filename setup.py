from readers.document_reader_factory import DocumentReaderFactory
from plahash import PlagiarismDetector
from utils.text_normalizer import TextNormalizer
from utils.block_creator import BlockCreator
from hashing.simple_hash import SimpleHash

def setup_plagiarism_detector(file_type):
    reader = DocumentReaderFactory.get_reader(file_type)
    if reader is None:
        return None
    normalizer = TextNormalizer()
    block_creator = BlockCreator()
    hash_function = SimpleHash()
    return PlagiarismDetector(reader, normalizer, block_creator, hash_function)

if __name__ == "__main__":
    detector = setup_plagiarism_detector('docx')
    if detector:
        result = detector.detect('path_to_file1.docx', 'path_to_file2.docx')
        print(f"Porcentagem de similaridade: {result['similarity_percentage']}")
        for block1, block2 in result['common_blocks']:
            print(f"Blocos comuns: {block1} | {block2}")
    else:
        print("Tipo de arquivo não suportado")