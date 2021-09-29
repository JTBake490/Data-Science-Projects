import unittest
from common_mappings import abbrev_country

class AbbrevCountry(unittest.TestCase):

    def test_uppercase_iso2(self):
        country = 'SPAIN'
        country_short = abbrev_country(country)
        expected = 'ES'
        self.assertEqual(country_short, expected)

    def test_lowercase_iso2(self):
        country = 'france'
        country_short = abbrev_country(country)
        expected = 'FR'
        self.assertEqual(country_short, expected)

    def test_mixedcase_iso2(self):
        country = 'Sao Tome and Principe'
        country_short = abbrev_country(country)
        expected = 'ST'
        self.assertEqual(country_short, expected)

    def test_get_iso3(self):
        country = 'Egypt'
        country_short = abbrev_country(country, abbrev='iso3')
        expected = 'EGY'
        self.assertEqual(country_short, expected)

    def test_get_uncode(self):
        country = 'Brazil'
        country_short = abbrev_country(country)
        expected = '076'
        self.assertTrue(country_short, expected)

    def test_bad_abbrev(self):
        country = 'JAMAICA'
        abbrev = 'ISO4'
        self.assertRaises(ValueError, abbrev_country, country, abbrev)

if __name__ == '__main__':
    unittest.main()
