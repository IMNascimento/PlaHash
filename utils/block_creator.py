class BlockCreator:
    def create_ngrams(self, text, n=3):
        words = text.lower().strip().split()
        ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
        return ngrams