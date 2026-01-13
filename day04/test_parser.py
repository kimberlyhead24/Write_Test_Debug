import unittest
from day04.parser import parse_user

class TestParseUser(unittest.TestCase):
    def test_valid_simple_line(self):
        self.assertEqual(parse_user("1,Robert,active"), {"id": 1, "name": "Robert", "status": "active"})

    def test_whitespace_is_stripped(self):
        self.assertEqual(parse_user("2 , Carolina, inactive"), {"id": 2, "name": "Carolina", "status": "inactive"})

    def test_invalid_id_raises(self):
        with self.assertRaises(ValueError):
            parse_user("three,Timothy,active")

    def test_wrong_field_count_raises(self):
        with self.assertRaises(ValueError):
            parse_user("4,Jerome,Powell,inactive")

if __name__ == "__main__":
    unittest.main()