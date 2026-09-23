from repository import UserRepository
class FileRepository(UserRepository):

    def save(self, user):
        with open("users.txt", "a") as file:
            file.write(user["name"] + "\n")

    def get_user(self, name):
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    if line.strip() == name:
                        return {"name": name}
        except FileNotFoundError:
            return None

        return None