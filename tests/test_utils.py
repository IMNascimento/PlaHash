from utils.text_normalizer import TextNormalizer
from utils.block_creator import BlockCreator

def test_text_normalizer():
    normalizer = TextNormalizer()
    result = normalizer.normalize("   Hello, WORLD! ")
    assert result == "hello world", "TextNormalizer failed to normalize text properly."

def test_block_creator():
    block_creator = BlockCreator()
    text = "one two three four five six"
    blocks = block_creator.create_blocks(text, 3)
    expected_blocks = ['one two three', 'two three four', 'three four five', 'four five six']
    assert blocks == expected_blocks, "BlockCreator failed to create blocks properly."