import unittest
from common_mappings import abbrev_directions

class AbbrevDirections(unittest.TestCase):

    def test_lowercase(self):
        direction = '12 degrees north'
        abbreviated = abbrev_directions(direction)
        expected = '12 degrees N'
        self.assertEqual(abbreviated, expected)

    def test_uppercase(self):
        direction = '20 DEG EAST'
        abbreviated = abbrev_directions(direction)
        expected = '20 DEG E'
        self.assertEqual(abbreviated, expected)

    def test_mixcase(self):
        direction = '15 D SouthWest'
        abbreviated = abbrev_directions(direction)
        expected = '15 D SW'
        self.assertEqual(abbreviated, expected)

    def test_compound(self):
        directions = 'South by SouthWest'
        abbreviated = abbrev_directions(directions)
        expected = 'S by SW'
        self.assertEqual(abbreviated, expected)

    def test_multiple_directions(self):
        directions = 'West 7 miles, turn right and head Northeast for 3 miles.'
        abbreviated = abbrev_directions(directions)
        expected = 'W 7 miles, turn right and head NE for 3 miles.'
        self.assertEqual(abbreviated, expected)

if __name__ == '__main__':
    unittest.main()