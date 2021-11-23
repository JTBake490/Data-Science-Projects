import unittest
from common_mappings import num_to_words

class TestNumToWords(unittest.TestCase):
    def test_0(self):
        num = 0
        expected = 'zero'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_7(self):
        num = 7
        expected = 'seven'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_15(self):
        num = 15
        expected = 'fifteen'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_20(self):
        num = 20
        expected = 'twenty'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_35(self):
        num = 35
        expected = 'thirty-five'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_88(self):
        num = 88
        expected = 'eighty-eight'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_100(self):
        num = 100
        expected = 'one-hundred'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_300(self):
        num = 300
        expected = 'three-hundred'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_789(self):
        num = 789
        expected = 'seven-hundred-eighty-nine'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_1000(self):
        num = 1_000
        expected = 'one-thousand'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_5000(self):
        num = 5_000
        expected = 'five-thousand'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_9382(self):
        num = 9372
        expected = 'nine-thousand-three-hundred-seventy-two'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_10000(self):
        num = 10_000
        expected = 'ten-thousand'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_40003(self):
        num = 40_003
        expected = 'fourty-thousand-three'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_200100607(self):
        num = 200_100_607
        expected = 'two-hundred-million-one-hundred-thousand-six-hundred-seven'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_3000000000(self):
        num = 3_000_000_000
        expected = 'three-billion'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_999_999_999_999_999(self):
        num = 999_999_999_999_999
        expected = 'nine-hundred-ninety-nine-trillion-nine-hundred-ninety-nine-billion-nine-hundred-ninety-nine-million-nine-hundred-ninety-nine-thousand-nine-hundred-ninety-nine'
        result = num_to_words(num)
        self.assertEqual(expected, result)

    def test_negative_number(self):
        num = -5
        self.assertRaises(AssertionError, num_to_words, num)

    def test_too_big_number(self):
        num = 12_345_678_901_234_567_890
        self.assertRaises(AssertionError, num_to_words, num)

if __name__ == '__main__':
    unittest.main()
