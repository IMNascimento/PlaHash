class SimpleHash:
    def hash(self, data):
        return sum(ord(char) for char in data) % 1000