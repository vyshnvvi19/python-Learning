from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):

    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def find_by_name(self, name):
        pass


class UserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users = []

    def save(self, user):
        self.users.append(user)

    def find_by_name(self, name):
        for user in self.users:
            if user["name"] == name:
                return user

        return None


class UserService:

    def __init__(self, repository):
        self.repository = repository

    def register_user(self, name, email):
        if "@" not in email:
            print("Invalid email")
            return

        user = {
            "name": name,
            "email": email
        }

        self.repository.save(user)
        print("User registered:", name)

    def find_user(self, name):
        return self.repository.find_by_name(name)


class EmailService:

    def send_email(self, name, message):
        print("Sending email to", name)
        print("Message:", message)


class ReportService:

    def generate_report(self, users):
        print("User Report")
        print("------------")

        for user in users:
            print("Name:", user["name"])
            print("Email:", user["email"])

        print("Total users:", len(users))


def calculate_total(price, quantity):
    return price * quantity


repository = UserRepository()
user_service = UserService(repository)
email_service = EmailService()
report_service = ReportService()


user_service.register_user(
    "Vyshnavi",
    "vyshnavi@gmail.com"
)

user_service.register_user(
    "Charan",
    "charan@gmail.com"
)


print(user_service.find_user("Vyshnavi"))


email_service.send_email(
    "Vyshnavi",
    "Welcome to the application"
)


print("Total:", calculate_total(500, 2))


report_service.generate_report(repository.users)
print("\n--- Error Case ---")

user_service.register_user(
    "Test User",
    "invalid-email"
)