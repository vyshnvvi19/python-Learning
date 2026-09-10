transactions = [
    {"category": "Food", "amount": 100},
    {"category": "Travel", "amount": 200},
    {"category": "Food", "amount": 50},
    {"category": "Shopping", "amount": 150}
]
total = {}
for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]
    if category in total:
        total[category] = total[category] + amount
    else:
        total[category] = amount
print(total)