class UserService:

    def __init__(self, repository):
        self.repository = repository

    def register_user(self, name):
        user = {"name": name}
        self.repository.save(user)

    def find_user(self, name):
        return self.repository.get_user(name)