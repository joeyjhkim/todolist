def todo():
    # initialize a empty list called task
    task = []
    # ask user to add task, remove task, show tasks, or quit
    print(
        "Joey's To-Do List \n would you like to  \n1. Add Task \n2. Remove Task \n3. Show Tasks \n4. Quit"
    )
    choice = input("Enter your choice (1, 2, or 3): ")
    while True:
        if choice == "1":
            # add task
            task.append(input("Enter the task: "))
            print("Task added. Would you like to add another task? (yes/no)")
            if input().lower() == "yes":
                choice = "1"
            else:
                choice = input(
                    "Enter your choice \n2. Remove Task \n3. Show Tasks \n4. Exit \n"
                )
        elif choice == "2":
            # remove task
            task.remove(input("Enter the task to remove: "))
            print("Task removed. Would you like to remove another task? (yes/no)")
            if input().lower() == "yes":
                choice = "2"
            else:
                choice = input(
                    "Enter your choice \n1. Add Task \n3. Show Tasks \n4. Exit \n"
                )
        elif choice == "3":
            # show tasks
            print("Your tasks are:")
            for i in range(len(task)):
                print(f"{i+1}. {task[i]}")
            print("Would you like to add or remove more tasks? (yes/no)")
            if input().lower() == "yes":
                choice = input("Enter your choice \n1. Add Task \n2. Remove Tasks \n")
            else:
                print("Would you like to exit? (yes/no)")
                if input().lower() == "yes":
                    choice == "4"
                    # quit
                    break
                else:
                    choice = input(
                        "Enter your choice \n1. Add Task \n2. Remove Tasks \n3. Show Tasks \n"
                    )
        elif choice == "4":
            # quit
            break
        else:
            print("Invalid choice. Please try again.")


todo()
