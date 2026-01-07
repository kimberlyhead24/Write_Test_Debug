import unittest
from day02.sum_positive import sum_positive


class TestSumPositive(unittest.TestCase):
    def test_no_element(self):
        self.assertEqual(sum_positive([]), 0)
    
    def test_all_positive(self):
        self.assertEqual(sum_positive([5, 10, 15, 23, 15, 7]), 75)

    def test_mixed_values(self):
        self.assertEqual(sum_positive([-1, 8, 15, 3, 0]), 26)

    def test_all_non_positive(self):
        self.assertEqual(sum_positive([0, -1, -20, 0, -30]), 0)

    def test_single_positive(self):
        self.assertEqual(sum_positive([-10, 8, 0, -25]), 8)

if __name__ == "__main__":
    unittest.main()