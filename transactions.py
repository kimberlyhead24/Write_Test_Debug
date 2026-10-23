def total_paid_amount(transactions, user_id):
    total = 0.0 
    for tx in transactions:
        if tx["user_id"] == user_id and tx["status"] == "paid":
            total += tx["amount"]
    return total


if __name__ == "__main__":
    sample_transactions = [
        {"user_id": 1, "amount": 10.0, "status": "paid"},
        {"user_id": 1, "amount": 5.0, "status": "refunded"},
        {"user_id": 2, "amount": 20.0, "status": "paid"},
    ]
    print("User 1 total:", total_paid_amount(sample_transactions, 1)) # expect 10.0
    print("User 2 total:", total_paid_amount(sample_transactions, 2)) # expect 20.0
    