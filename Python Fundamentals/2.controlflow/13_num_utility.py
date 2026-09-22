while True:
    print("1. Square")
    print("2. Cube")
    print("3. Even or Odd")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "4":
        print("Goodbye!")
        break

    elif choice == "1":
        num = int(input("Enter number: "))
        print("Square:", num ** 2)

    elif choice == "2":
        num = int(input("Enter number: "))
        print("Cube:", num ** 3)

    elif choice == "3":
        num = int(input("Enter number: "))

        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")