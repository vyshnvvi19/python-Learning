from utils.validation import validate_email


class UserService:

    def __init__(self, repository):
        self.repository = repository

    def register_user(self, name, email):
        if not validate_email(email):
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