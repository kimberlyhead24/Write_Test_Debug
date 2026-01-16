import unittest
from day06.normalizer_debug import normalize_user

class TestNormalizerUser(unittest.TestCase):
    def test_valid_payload_bool_active(self):
        payload = {
            "id": 1, 
            "name": " Cheryl Rodgers ", 
            "age": 18, 
            "active": True,
        }
        expected = {
            "id": 1, 
            "name": "Cheryl Rodgers", 
            "age": 18, 
            "status": "active",  
        }
        self.assertEqual(normalize_user(payload), expected)
    
    def test_valid_payload_string_active(self):
        payload = {
            "id": 2,
            "name": "   Kimber Head  ",
            "age": 37,
            "active": "false",
        }
        expected = {
            "id": 2,
            "name": "Kimber Head",
            "age": 37,
            "status": "inactive",
        }
        self.assertEqual(normalize_user(payload), expected)

    def test_missing_field_raises(self):
        payload = {
            "id": 3,
            "age": 28,
            "active": False,
        }
        with self.assertRaises(ValueError):
            normalize_user(payload)

    def test_invalid_id_raises(self):
        payload = {
            "id": "four",
            "age": 45,
            "active": True,
        }
        with self.assertRaises(ValueError):
            normalize_user(payload)

    def test_invalid_active_raises(self):
        payload = {
            "id": 5,
            "name": "   Evelyn Hardly ",
            "age": 55,
            "active": "yes",
        }
        with self.assertRaises(ValueError):
            normalize_user(payload)


if __name__ == "__main__":
    unittest.main()