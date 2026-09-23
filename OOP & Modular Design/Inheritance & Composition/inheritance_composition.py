from abc import ABC, abstractmethod


# Notification uses inheritance and abstract behavior
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("[Email]", message)


class SMSNotification(Notification):
    def send(self, message):
        print("[SMS]", message)


# Payment uses composition
class CardPayment:
    def pay(self, amount):
        print("Paid", amount, "by card")


class PayPalPayment:
    def pay(self, amount):
        print("Paid", amount, "via PayPal")


class Checkout:
    def __init__(self, method):
        self.method = method

    def pay(self, amount):
        self.method.pay(amount)

    def switch_method(self, new_method):
        self.method = new_method


# Reporting uses both inheritance and composition
class Report(ABC):
    def __init__(self, formatter):
        self.formatter = formatter

    @abstractmethod
    def gather_data(self):
        pass

    def show(self):
        data = self.gather_data()
        print(self.formatter.format(data))


class SalesReport(Report):
    def gather_data(self):
        return {"total_sales": 15000}


class InventoryReport(Report):
    def gather_data(self):
        return {"items_in_stock": 240}


class TextFormatter:
    def format(self, data):
        return "\n".join(f"{key}: {value}" for key, value in data.items())


class HTMLFormatter:
    def format(self, data):
        rows = "".join(
            f"<tr><td>{key}</td><td>{value}</td></tr>"
            for key, value in data.items()
        )
        return f"<table>{rows}</table>"


# Test notification
print("--- Notification ---")
EmailNotification().send("Order shipped")
SMSNotification().send("Order shipped")


# Test payment
print("\n--- Payment ---")
checkout = Checkout(CardPayment())
checkout.pay(100)

checkout.switch_method(PayPalPayment())
checkout.pay(50)


# Test reporting
print("\n--- Reporting ---")
sales = SalesReport(TextFormatter())
sales.show()

inventory = InventoryReport(HTMLFormatter())
inventory.show()