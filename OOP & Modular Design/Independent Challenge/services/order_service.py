from domain.order import Order


class OrderService:

    def __init__(self, repository):
        self.repository = repository

    def create_order(
        self,
        order_id,
        customer_name,
        product_name,
        quantity,
        price
    ):
        if not customer_name:
            raise ValueError("Customer name is required")

        if not product_name:
            raise ValueError("Product name is required")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        order = Order(
            order_id,
            customer_name,
            product_name,
            quantity,
            price
        )

        self.repository.save(order)

        return order

    def find_order(self, order_id):
        return self.repository.find_by_id(order_id)

    def get_all_orders(self):
        return self.repository.get_all()