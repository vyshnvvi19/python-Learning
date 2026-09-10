choice = 0
while choice != 4:
    print("1. Name")
    print("2. Marks")
    print("3. College")
    print("4. Exit")

    choice = int(input("Choose: "))

    if choice == 1:
        print("Name selected")
    elif choice == 2:
        print("Marks selected")
    elif choice == 3:
        print("College selected")
    else:
        print("Exit")