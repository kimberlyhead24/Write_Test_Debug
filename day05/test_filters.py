import unittest
from day05.filters_debug import filter_users

class TestFilterUsers(unittest.TestCase):
    def test_no_filters_returns_all(self):
        users = [
            {"id": 1, "name": "Maurice John", "age": 24, "status": "active"}, 
            {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"}, 
            {"id": 3, "name": "BamBam Muenster", "age": 14, "status": "inactive"},
        ]
        self.assertEqual(
            filter_users(users), 
            [
                {"id": 1, "name": "Maurice John", "age": 24, "status": "active"}, 
                {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"},
                {"id": 3, "name": "BamBam Muenster", "age": 14, "status": "inactive"},
            ],
        )

    def test_filter_by_min_age_only(self):
        users = [
            {"id": 1, "name": "Maurice John", "age": 24, "status": "active"}, 
            {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"}, 
            {"id": 3, "name": "BamBam Muenster", "age": 14, "status": "inactive"},
        ]
        self.assertEqual(
            filter_users(users, min_age=25),
            [
                {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"},
            ]
        )          
    def test_filter_by_status_only(self):
        users = [
            {"id": 1, "name": "Maurice John", "age": 24, "status": "active"}, 
            {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"}, 
            {"id": 3, "name": "BamBam Muenster", "age": 14, "status": "inactive"},
        ]
        self.assertEqual(
            filter_users(users, status="active"),
            [
                {"id": 1, "name": "Maurice John", "age": 24, "status": "active"},
                {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"},
            ]
        )  

    def test_filter_by_both_age_and_status(self):
        users = [
            {"id": 1, "name": "Maurice John", "age": 24, "status": "active"}, 
            {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"}, 
            {"id": 3, "name": "BamBam Muenster", "age": 14, "status": "inactive"},
        ]
        self.assertEqual(
            filter_users(users, min_age=10, status="inactive"),
            [
                {"id": 3, "name": "BamBam Muenster", "age": 14, "status": "inactive"},
            ]
        )  

    def test_no_user_matches(self):
        users = [
            {"id": 1, "name": "Maurice John", "age": 24, "status": "active"}, 
            {"id": 2, "name": "Kimberly Jonas", "age": 35, "status": "active"}, 
            {"id": 3, "name": "BamBam Muenster", "age": 14, "status": "inactive"},
        ]
        self.assertEqual(
            filter_users(users, min_age=20, status="inactive"), []) 

if __name__ == "__main__":
    unittest.main()
