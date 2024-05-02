from utils.text_normalizer import TextNormalizer
from utils.block_creator import BlockCreator
from hashing.simple_hash import SimpleHash

class PlagiarismDetector:
    def __init__(self, reader, normalizer, block_creator, hash_function):
        self.reader = reader
        self.normalizer = normalizer
        self.block_creator = block_creator
        self.hash_function = hash_function

    def detect(self, file1, file2):
        text1 = self.normalizer.normalize(self.reader.read(file1))
        text2 = self.normalizer.normalize(self.reader.read(file2))

        blocks1 = self.block_creator.create_blocks(text1)
        blocks2 = self.block_creator.create_blocks(text2)

        hashes1 = {self.hash_function.hash(block): block for block in blocks1}
        hashes2 = {self.hash_function.hash(block): block for block in blocks2}

        common_hashes = set(hashes1.keys()) & set(hashes2.keys())
        similarity = len(common_hashes) / len(hashes1) * 100

        return {
            'similarity_percentage': similarity,
            'common_blocks': [(hashes1[h], hashes2[h]) for h in common_hashes]
        }