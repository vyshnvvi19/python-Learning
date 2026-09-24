from repositories.mock_order_repository import MockOrderRepository
from services.order_service import OrderService


repository = MockOrderRepository()
service = OrderService(repository)


order = service.create_order(
    "ORD001",
    "Vyshnavi",
    "Laptop",
    2,
    50000
)

print("Order ID:", order.order_id)
print("Customer:", order.customer_name)
print("Product:", order.product_name)
print("Quantity:", order.quantity)
print("Price:", order.price)
print("Total:", order.calculate_total())

print("\nFind Order:")
print(service.find_order("ORD001"))