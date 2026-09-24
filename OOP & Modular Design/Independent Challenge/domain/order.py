class Order:

    def __init__(self, order_id, customer_name, product_name, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        return self.quantity * self.price

    def __str__(self):
        return (
            f"Order ID: {self.order_id}, "
            f"Customer: {self.customer_name}, "
            f"Product: {self.product_name}, "
            f"Quantity: {self.quantity}, "
            f"Total: {self.calculate_total()}"
        )