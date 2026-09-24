from config.settings import APP_NAME
from repositories.user_repository import UserRepository
from services.user_service import UserService


print(APP_NAME)

repository = UserRepository()
service = UserService(repository)

service.register_user("Vyshnavi", "vyshnavi@gmail.com")
service.register_user("Charan", "charan@gmail.com")

print(service.find_user("Vyshnavi"))