def validate_password(password):
    if password == "":
        raise ValueError("Password cannot be empty")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one number")

    print("Password is valid")
try:
    password = input("Enter password: ")
    validate_password(password)

except ValueError as e:
    print("Error:", e)