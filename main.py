try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
    
except FileNotFoundError:
    tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Mark Completed")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}.{task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}.{task}")

            delete_task = int(input("Enter task number to delete: "))
            if 1 <= delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                with open("tasks.txt","w") as file:
                    for task in tasks:file.write(task + "\n")
                print(f"Deleted:{removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i, task in enumerate(tasks):
               print(f"{i + 1}.{task}")

            completed_task = int(input("Enter task number to completed: "))
            if 1 <= completed_task <= len(tasks):
                tasks[completed_task - 1] += "[Completed]"
                with open("tasks.txt","w")as file:
                    for task in tasks:
                        file.write(task + "\n")
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Existing program...")
        break

    else:
        print("Invalid choice.")




