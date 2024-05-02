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
    detector = setup_plagiarism_detector('pdf')
    if detector:
        result = detector.detect('artigo-2017.pdf', 'artigo-LSTM-revolucionario.pdf')
        
        print("Blocos comuns de n-gramas:")
        i = 0
        for ngram1, ngram2 in result['common_ngrams']:
            print(f"Blocos {i}: {ngram1} | {ngram2}")
            i += 1
        print(f"Porcentagem de similaridade: {result['similarity_percentage']:.2f}%")
    else:
        print("Tipo de arquivo não suportado")