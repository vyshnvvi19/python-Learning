inventory={
    "apple":{"Quantity":10,"Price":3},
    "mango":{"Quantity":12,"Price":4},
    "banana":{"Quantity":16,"Price":9}
}
print("Inventory: ",inventory)
item=input("Enter the item: ")
if item in inventory:
    print("Quantity: ",inventory[item]["Quantity"])
    print("Price: ",inventory[item]["Price"])
else:
    print("Item not found")
total=0
for item in inventory:
    total=total+inventory[item]["Quantity"]*inventory[item]["Price"]
print("Total: ",total)


