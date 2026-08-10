tasks = []
while True:
    print("===TO-DO LIST ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exist")

    choice =input("choose an option:")
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Task:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task}")
    elif choice == "2":
        task = input("Enter task:")
        tasks.append(task)
        print("Task added successfully")

    elif choice == "3":
        task = input("Enter the task to remove:")
        if task in tasks:
            tasks.remove(task)
            print("Task remove successfully")
        else:
            print("Task not found.")

    elif choice =="4":
        print("Goodbye!")
        break

    else:
        print("invalid option please choose1,2,3,or 4.")               
