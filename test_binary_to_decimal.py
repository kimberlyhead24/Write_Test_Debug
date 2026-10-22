import unittest
from binary_to_decimal import to_decimal

class TestToDecimal(unittest.TestCase):
    def test_valid_binary(self):
        self.assertEqual(to_decimal("1010"), 10)
        self.assertEqual(to_decimal("1111"), 15)
        self.assertEqual(to_decimal("0"), 0)
        self.assertEqual(to_decimal("1"), 1)
        self.assertEqual(to_decimal("101010"), 42)
        self.assertEqual(to_decimal("110011"), 51)
        self.assertEqual(to_decimal("10101010"), 170)
        self.assertEqual(to_decimal("11111111"), 255)

    def test_invalid_binary(self):
        with self.assertRaises(ValueError):
            to_decimal("2")
        with self.assertRaises(ValueError):
            to_decimal("abc")
        with self.assertRaises(ValueError):
            to_decimal("102")
        with self.assertRaises(ValueError):
            to_decimal("10 2")
        with self.assertRaises(ValueError):
            to_decimal("10\n2")

if __name__ == "__main__":
    unittest.main()