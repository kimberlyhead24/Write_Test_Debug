import unittest
from day03.transactions_debug import total_paid_amount

class TestTotalPaidAmount(unittest.TestCase):
    def test_no_transactions(self):
        self.assertEqual(total_paid_amount([], 1), 0.0)
    
    def test_no_paid_for_user(self):
        transactions = [
            {"user_id": 1, "amount": 15.0, "status": "refunded"}, 
            {"user_id": 2, "amount": 6.0, "status": "refunded"}, 
            {"user_id": 1, "amount": 35.0, "status": "refunded"},
        ]

        self.assertEqual(total_paid_amount(transactions, 1), 0.0)
    
    def test_only_paid_for_user(self):
        transactions = [
            {"user_id": 1, "amount": 15.0, "status": "paid"}, 
            {"user_id": 2, "amount": 6.0, "status": "paid"}, 
            {"user_id": 1, "amount": 35.0, "status": "paid"},
        ]
        self.assertEqual(total_paid_amount(transactions, 1), 50.0)
    
    def test_mixed_statuses_for_user(self):
        transactions = [
            {"user_id": 1, "amount": 15.0, "status": "paid"},
            {"user_id": 2, "amount": 6.0, "status": "refunded"},
            {"user_id": 2, "amount": 35.0, "status": "paid"}
    
        ]
        self.assertEqual(total_paid_amount(transactions, 1), 15.0)

    def test_multiple_users(self):
        transactions = [
            {"user_id": 1, "amount": 15.0, "status": "paid"}, 
            {"user_id": 2, "amount": 6.0, "status": "paid"}, 
            {"user_id": 1, "amount": 35.0, "status": "refunded"}, 
            {"user_id": 2, "amount": 13.0, "status": "refunded"}

        ]
        self.assertEqual(total_paid_amount(transactions, 1), 15.0)

if __name__ == "__main__":
    unittest.main()