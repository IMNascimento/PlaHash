class BlockCreator:
    def create_blocks(self, text, block_size=5):
        words = text.split()
        return [" ".join(words[i:i + block_size]) for i in range(len(words) - block_size + 1)]