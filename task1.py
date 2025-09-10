tasks = []

def display_tasks():
    if len(tasks) == 0:
        print("\nYou currently have no tasks.")
    else:
        print("\nList of Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def create_task():
    task = input("Enter a task to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' has been added successfully.")
    else:
        print("Cannot add an empty task.")

def remove_task():
    display_tasks()
    if len(tasks) > 0:
        try:
            task_no = int(input("Enter the task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed}' has been deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def run_todo_list():
    print("Welcome to your To-Do List App!")
    while True:
        print("\nMenu Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_tasks()
        elif choice == "2":
            create_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the To-Do List. Have a productive day!")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    run_todo_list()
