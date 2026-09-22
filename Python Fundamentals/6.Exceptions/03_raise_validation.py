def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age > 120:
        raise ValueError("Age cannot be greater than 120")

    print("Valid age")
try:
    age = int(input("Enter your age: "))
    validate_age(age)

except ValueError as e:
    print("Error:", e)