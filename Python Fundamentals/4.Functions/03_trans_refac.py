transactions = [
    {"category": "Food", "amount": 100},
    {"category": "Travel", "amount": 200},
    {"category": "Food", "amount": 50},
    {"category": "Shopping", "amount": 150}
]
def calculate_totals(transactions):
    total = {}

    for transaction in transactions:
        category = transaction["category"]
        amount = transaction["amount"]

        if category in total:
            total[category] = total[category] + amount
        else:
            total[category] = amount

    return total
result = calculate_totals(transactions)
print(result)