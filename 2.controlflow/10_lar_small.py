numbers = [4, 8, 15, 16, 23, 42, 7, 9]
largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest:", largest)
print("Smallest:", smallest)