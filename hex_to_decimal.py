import unittest

def hex_to_decimal(hex: str) -> int:
    total = 0
    hex_key = [
        ("A", 10), ("B", 11), ("C", 12),
        ("D", 13), ("E", 14), ("F", 15)
        ]
    for character in hex:
        try:
            value = int(character)
        except ValueError:
            for letter, num in hex_key:
                if character == letter:
                    value = num
                    break
        total = total * 16 + value

    return total

class TestHexToDecimal(unittest.TestCase):
    def test_single_letter(self):
        self.assertEqual(hex_to_decimal("A"), 10)
    def test_two_numbers(self):
        self.assertEqual(hex_to_decimal("15"), 21)
    def test_letter_number(self):
        self.assertEqual(hex_to_decimal("2E"), 46)
    def test_zero(self):
        self.assertEqual(hex_to_decimal("0"), 0)
    def test_length_of_three(self):
        self.assertEqual(hex_to_decimal("234"), 564)
    def test_normal_numbers(self):
        self.assertEqual(hex_to_decimal("23"), 36)
    def test_normal_letters(self):
        self.assertEqual(hex_to_decimal("FF"), 255)
    
 
