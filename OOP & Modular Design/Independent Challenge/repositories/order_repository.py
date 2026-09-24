from abc import ABC, abstractmethod


class OrderRepository(ABC):

    @abstractmethod
    def save(self, order):
        pass

    @abstractmethod
    def find_by_id(self, order_id):
        pass

    @abstractmethod
    def get_all(self):
        pass