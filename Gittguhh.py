def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

        def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!\n")


def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("type number to delete: "))
            removed = tasks.pop(task_num - 1)
            print(f"Removed task: {removed}\n")
        except (ValueError, IndexError):
            print("Invalid task number.\n")

def main():
    tasks = []

    while True:
        print("")
        print("")
        print("")
        print("")
        print("")

        choice = input("")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
