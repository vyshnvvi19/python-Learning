numbers = [4, 8, 15, 16, 23, 42, 7, 9]
target = int(input("Enter number to search for: "))
for n in numbers:
    if n == target:
        print("Found:", n)
        break
else:
    print("Not found")