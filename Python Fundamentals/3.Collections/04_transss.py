transactions = [
    {"type": "deposit", "amount": 1000},
    {"type": "withdraw", "amount": 200},
    {"type": "deposit", "amount": 500},
    {"type": "withdraw", "amount": 100}
]
totals = {
    "deposit": 0,
    "withdraw": 0
}
for transaction in transactions:
    if transaction["type"] == "deposit":
        totals["deposit"] = totals["deposit"] + transaction["amount"]
    else:
        totals["withdraw"] = totals["withdraw"] + transaction["amount"]
print(totals)