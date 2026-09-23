class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Used to read the price
    @property
    def price(self):
        return self._price

    # Used to control changes to the price
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")

        self._price = value

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)


class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    # Used to read the quantity
    @property
    def quantity(self):
        return self._quantity

    # Used to control changes to the quantity
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity must be greater than 0")

        self._quantity = value

    def calculate_total(self):
        return self.product.price * self.quantity

    def display(self):
        print("Product:", self.product.name)
        print("Quantity:", self.quantity)
        print("Total:", self.calculate_total())


# Create a valid Product object
product1 = Product("Laptop", 50000)

# Create a valid Order object
order1 = Order(product1, 2)


# Display valid data
print("Product Details")
print("----------------")
product1.display()

print("\nOrder Details")
print("-------------")
order1.display()


# Test invalid price
try:
    product1.price = -100
except ValueError as error:
    print("\nBlocked:", error)


# Test invalid quantity
try:
    order1.quantity = 0
except ValueError as error:
    print("Blocked:", error)