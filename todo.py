def load_tasks(filename):
   
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(filename, tasks):

    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()


def add_task(tasks):
    
    task = input("Enter the new task: ")
    tasks.append(task)
    print("Task added.\n")


def remove_task(tasks):
    
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(filename, tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(filename, tasks)
        elif choice == "4":
            save_tasks(filename, tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-4.\n")


if __name__ == "__main__":
    main()