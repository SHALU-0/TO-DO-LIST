tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Saved!")

    elif choice == "2":
        print("Your tasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Wrong choice!")
