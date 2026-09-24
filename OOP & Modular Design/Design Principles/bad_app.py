class UserManager:

    def __init__(self):
        self.users = []

    def register_user(self, name, email):
        if "@" not in email:
            print("Invalid email")
            return

        user = {
            "name": name,
            "email": email
        }

        self.users.append(user)
        print("User registered:", name)

    def find_user(self, name):
        for user in self.users:
            if user["name"] == name:
                return user

        return None

    def send_email(self, name, message):
        print("Sending email to", name)
        print("Message:", message)

    def calculate_total(self, price, quantity):
        return price * quantity

    def generate_report(self):
        print("User Report")
        print("------------")

        for user in self.users:
            print("Name:", user["name"])
            print("Email:", user["email"])

        print("Total users:", len(self.users))


manager = UserManager()

manager.register_user("Vyshnavi", "vyshnavi@gmail.com")
manager.register_user("Charan", "charan@gmail.com")

print(manager.find_user("Vyshnavi"))

manager.send_email(
    "Vyshnavi",
    "Welcome to the application"
)

print("Total:", manager.calculate_total(500, 2))

manager.generate_report()