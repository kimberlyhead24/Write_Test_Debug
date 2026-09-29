import unittest
from day07.spam_filter import is_spam

class TestSpamFilter(unittest.TestCase):
    def test_no_spam_single_countrycode(self):
        number = "+0 (200) 234-0182"
        expected = False
        self.assertEqual(is_spam(number), expected)
    
    def test_spam_countrycode(self):
        number = "+091 (555) 309-1922"
        expected = True
        self.assertEqual(is_spam(number), expected)

    def test_spam_no_leading_zero(self):
        number = "+1 (555) 435-4792"
        expected = True
        self.assertEqual(is_spam(number), expected)

    def test_spam_large_areacode(self):
        number = "+0 (955) 234-4364"
        expected = True
        self.assertEqual(is_spam(number), expected)

    def test_spam_small_areacode(self):
        number = "+0 (155) 131-6943"
        expected = True
        self.assertEqual(is_spam(number), expected)

    def test_spam_sum_local_end(self):
        number = "+0 (555) 135-0192"
        expected = True
        self.assertEqual(is_spam(number), expected)

    def test_spam_repeating_digits(self):
        number = "+0 (555) 564-1987"
        expected = True
        self.assertEqual(is_spam(number), expected)

    def test_no_spam_double_countrycode(self):
        number = "+00 (555) 234-0182"
        expected = False
        self.assertEqual(is_spam(number), expected)


if __name__ == "__main__":
    unittest.main()
