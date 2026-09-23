from memory_repository import MemoryRepository
from file_repository import FileRepository
from service import UserService


print("--- Memory Repository ---")

memory_repository = MemoryRepository()
memory_service = UserService(memory_repository)

memory_service.register_user("Vyshnavi")

print(memory_service.find_user("Vyshnavi"))


print("\n--- File Repository ---")

file_repository = FileRepository()
file_service = UserService(file_repository)

file_service.register_user("Charan")

print(file_service.find_user("Charan"))