class InsufficientBalanceError(Exception):
    pass
balance = 5000
try:
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance = balance - amount

    print("Withdrawal successful")
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid amount")