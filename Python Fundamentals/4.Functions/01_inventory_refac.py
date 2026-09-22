inventory = {
    "apple": {"Quantity": 10, "Price": 3},
    "mango": {"Quantity": 12, "Price": 4},
    "banana": {"Quantity": 16, "Price": 9}
}
def show_inventory():
    print("Inventory:", inventory)
def find_item(item):
    if item in inventory:
        print("Quantity:", inventory[item]["Quantity"])
        print("Price:", inventory[item]["Price"])
    else:
        print("Item not found")
def calculate_total():
    total = 0

    for item in inventory:
        total = total + inventory[item]["Quantity"] * inventory[item]["Price"]
    return total
show_inventory()
item = input("Enter the item: ")
find_item(item)
total = calculate_total()
print("Total:", total)