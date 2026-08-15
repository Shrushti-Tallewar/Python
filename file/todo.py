# todo.py

tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task():
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print(" Task cannot be empty.")


def delete_task():
    show_tasks()

    if not  tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f" Deleted: {removed}")
        else:
            print(" Invalid task number.")

    except ValueError :
        print(" Please enter a valid number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye! ")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
