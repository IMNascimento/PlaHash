from hashing.simple_hash import SimpleHash

def test_simple_hash():
    hasher = SimpleHash()
    result = hasher.hash("hello")
    assert result == sum(ord(c) for c in "hello") % 1000, "SimpleHash failed to hash correctly."