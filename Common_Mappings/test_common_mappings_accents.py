import unittest
from common_mappings import remove_accents

class TestRemoveAccents(unittest.TestCase):

    def test_single_lowercase_translate(self):
        letter = 'è'
        ascii_letter = 'e'
        letter_translated = remove_accents(letter)
        self.assertEqual(letter_translated, ascii_letter)

    def test_single_uppercase_translate(self):
        letter = 'Ñ'
        ascii_letter = 'N'
        letter_translated = remove_accents(letter)
        self.assertEqual(letter_translated, ascii_letter)

    def test_D_or_E(self):
        letters = 'ĐÐĐÐ'
        ascii_letters = 'DEDE'
        letters_translated = remove_accents(letters)
        self.assertEqual(letters_translated, ascii_letters, msg='Should Be DEDE')

    def test_word_lowercase(self):
        word = 'băsš'
        word_ascii = 'bass'
        word_translated = remove_accents(word)
        self.assertEqual(word_translated, word_ascii)

    def test_word_uppercase(self):
        word = 'ĞÂĐĠEȚ'
        word_ascii = 'GADGET'
        word_translated = remove_accents(word)
        self.assertEqual(word_translated, word_ascii)

    def test_word_mixedcase(self):
        word = 'ÔpēŅed'
        word_ascii = 'OpeNed'
        word_translated = remove_accents(word)
        self.assertEqual(word_translated, word_ascii)

    def test_sentence_one(self):
        sentence = 'Þàčk Mý Bŏx Ẁîth FivÐ Đożen Liquor Jugs'
        sentence_ascii = 'Pack My Box With FivE Dozen Liquor Jugs'
        sentence_translated = remove_accents(sentence)
        self.assertEqual(sentence_translated, sentence_ascii)

    def test_sentence_two(self):
        sentence = 'The Quick Brown Főx Jūmps Oveŗ The Lazy Ďœg'
        sentence_ascii = 'The Quick Brown Fox Jumps Over The Lazy Dog'
        sentence_translated = remove_accents(sentence)
        self.assertEqual(sentence_translated, sentence_ascii)

if __name__ == '__main__':
    unittest.main()