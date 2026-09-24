class UserRepository:

    def __init__(self):
        self.users = []

    def save(self, user):
        self.users.append(user)

    def find_by_name(self, name):
        for user in self.users:
            if user["name"] == name:
                return user

        return None