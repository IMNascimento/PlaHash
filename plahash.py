from utils.text_normalizer import TextNormalizer
from utils.block_creator import BlockCreator
from hashing.simple_hash import SimpleHash

class PlagiarismDetector:
    def __init__(self, reader, normalizer, block_creator, hash_function):
        self.reader = reader
        self.normalizer = normalizer
        self.block_creator = block_creator  # Não será mais usado diretamente
        self.hash_function = hash_function  # Não será mais usado diretamente

    def detect(self, file1, file2, n=1):
        # Lê e normaliza os textos
        text1 = self.normalizer.normalize(self.reader.read(file1))
        text2 = self.normalizer.normalize(self.reader.read(file2))
        
        # Calcula a similaridade e obtém n-gramas comuns
        similarity, common_ngrams = self.calculate_similarity(text1, text2, n)
        
        return {
            'similarity_percentage': similarity * 100,
            'common_ngrams': common_ngrams
        }
    
    def calculate_similarity(self, text1, text2, n=3):
        block_creator = BlockCreator()
        hasher = SimpleHash()
        
        ngrams1 = block_creator.create_ngrams(text1, n)
        ngrams2 = block_creator.create_ngrams(text2, n)
        
        hash_to_ngrams1 = {hasher.hash(ngram): ngram for ngram in ngrams1}
        hash_to_ngrams2 = {hasher.hash(ngram): ngram for ngram in ngrams2}
        
        # Interseção dos hashes para encontrar n-gramas comuns
        common_hashes = set(hash_to_ngrams1.keys()) & set(hash_to_ngrams2.keys())
        common_ngrams = [(hash_to_ngrams1[h], hash_to_ngrams2[h]) for h in common_hashes]
        
        # Cálculo da similaridade
        union_hashes = set(hash_to_ngrams1.keys()) | set(hash_to_ngrams2.keys())
        similarity = len(common_hashes) / len(union_hashes) if union_hashes else 0
        
        return similarity, common_ngrams