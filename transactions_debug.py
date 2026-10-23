def total_paid_amount(transactions, user_id):
    total = 0.0
    for tx in transactions:
        # BUG: forgot to check user_id
        if tx["status"] == "paid":  # added user_id check to if statement
            total += tx["amount"]
    return total
