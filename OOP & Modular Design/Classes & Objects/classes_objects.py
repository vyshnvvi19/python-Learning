class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_details(self):
        print("Customer Name:", self.name)
        print("Email:", self.email)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        print("Product Name:", self.name)
        print("Price:", self.price)


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity


class Invoice:
    def __init__(self, invoice_number, order):
        self.invoice_number = invoice_number
        self.order = order

    def display_invoice(self):
        print("Invoice Number:", self.invoice_number)
        print("Customer:", self.order.customer.name)
        print("Product:", self.order.product.name)
        print("Quantity:", self.order.quantity)
        print("Total Amount:", self.order.calculate_total())


# Creating Customer object
customer1 = Customer("Vyshnavi", "vyshnavi@gmail.com")

# Creating Product object
product1 = Product("Laptop", 50000)

# Creating Order object
order1 = Order(customer1, product1, 2)

# Creating Invoice object
invoice1 = Invoice("INV001", order1)


# Display details
customer1.display_details()

print()

product1.display_details()

print()

invoice1.display_invoice()