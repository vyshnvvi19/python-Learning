def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid email")
def validate_amount(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
def validate_phone(phone):
    if len(phone) != 10 or not phone.isdigit():
        raise ValueError("Invalid phone number")

try:
    age = int(input("Enter age: "))
    validate_age(age)

    email = input("Enter email: ")
    validate_email(email)

    amount = float(input("Enter amount: "))
    validate_amount(amount)

    phone = input("Enter phone number: ")
    validate_phone(phone)

    print("All details are valid")

except ValueError as e:
    print("Error:", e)