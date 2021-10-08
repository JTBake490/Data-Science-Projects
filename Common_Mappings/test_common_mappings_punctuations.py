import unittest
from common_mappings import remove_punctuation

class TestRemovePunctuation(unittest.TestCase):

    def test_simple_sentence(self):
        text = "What's he doing over there?"
        expected = 'Whats he doing over there'
        text_processed = remove_punctuation(text)
        self.assertEqual(expected, text_processed)

    def test_different_seperator(self):
        text = "What's he doing over there?"
        expected = 'What s he doing over there'
        text_processed = remove_punctuation(text, sep=' ')
        self.assertEqual(expected, text_processed)

if __name__ == '__main__':
    unittest.main()