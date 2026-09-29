import unittest
from day07.spam_filter import is_spam

class TestSpamFilter(unittest.TestCase):
    def test_notSpam_singleCountryCode(self):
        self.assertFalse(is_spam("+0 (200) 234-0182"))
    
    def test_spam_countryCodeLarge(self):
        self.assertTrue(is_spam("+091 (555) 309-1922"))

    def test_spam_noLeadingZero(self):
        self.assertTrue(is_spam("+1 (555) 435-4792"))

    def test_spam_largeAreacode(self):
        self.assertTrue(is_spam("+0 (955) 234-4364"))

    def test_spam_smallAreacode(self):
        self.assertTrue(is_spam("+0 (155) 131-6943"))

    def test_spam_sumLocalStartInEnd(self):
        self.assertTrue(is_spam("+0 (555) 135-0192"))

    def test_spam_repeatingDigits(self):
        self.assertTrue(is_spam("+0 (555) 564-1987"))

    def test_notSpam_doubleCountryCode(self):
        self.assertFalse(is_spam("+00 (555) 234-0182"))

    def test_notSpam_repeatingDigits(self):
        self.assertFalse(is_spam("+08 (309) (555-3254)"))
    


if __name__ == "__main__":
    unittest.main()
