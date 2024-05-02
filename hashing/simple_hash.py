class SimpleHash:
    def hash(self, data):
        ascii_sum = sum(ord(char) for char in data)
        unique_chars = len(set(data))
        hash_value = (ascii_sum * unique_chars) % 1000
        return hash_value