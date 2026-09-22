def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return True
try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Valid age")

except ValueError as e:
    print("Error:", e)