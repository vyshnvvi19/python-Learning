from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def get_user(self, name):
        pass