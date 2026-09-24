from repositories.order_repository import OrderRepository


class MockOrderRepository(OrderRepository):

    def __init__(self):
        self.orders = []

    def save(self, order):
        self.orders.append(order)

    def find_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order

        return None

    def get_all(self):
        return self.orders