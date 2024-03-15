def add_task(todo_list):
    task_description = input("Enter task description: ")
    task = {"description": task_description, "completed": False, "priority": None}
    todo_list.append(task)
    print("Task added successfully.")

def mark_completed(todo_list):
    print("Current To-Do List:")
    display_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to mark as completed: "))
        if 0 <= index < len(todo_list):
            todo_list[index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer index.")

def view_todo_list(todo_list):
    if not todo_list:
        print("To-Do List is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            print(f"{index}. {task['description']} - {'Completed' if task['completed'] else 'Pending'} - Priority: {task['priority']}")

def prioritize_task(todo_list):
    print("Current To-Do List:")
    display_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to prioritize: "))
        if 0 <= index < len(todo_list):
            priority = input("Enter the priority level (high, medium, low): ")
            if priority.lower() in ['high', 'medium', 'low']:
                todo_list[index]["priority"] = priority.lower()
                print("Priority set successfully.")
            else:
                print("Invalid priority level. Please enter high, medium, or low.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer index.")

def remove_completed_tasks(todo_list):
    completed_tasks = [task for task in todo_list if task["completed"]]
    if completed_tasks:
        todo_list[:] = [task for task in todo_list if not task["completed"]]
        print("Removed Completed Tasks:")
        for task in completed_tasks:
            print(task["description"])
    else:
        print("There are no completed tasks to remove.")

def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View To-Do List")
    print("4. Prioritize Task")
    print("5. Remove Completed Tasks")
    print("6. Exit")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            mark_completed(todo_list)
        elif choice == "3":
            view_todo_list(todo_list)
        elif choice == "4":
            prioritize_task(todo_list)
        elif choice == "5":
            remove_completed_tasks(todo_list)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()