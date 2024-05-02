import re

class TextNormalizer:
    def normalize(self, text):
        return re.sub(r'\W+', ' ', text.lower()).strip()