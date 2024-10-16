import json
import os

# Define the Task class
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'completed': self.completed}

# Load tasks from a file (tasks.json)
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks_data = json.load(file)
            # Map 'id' from JSON data to 'task_id' in Task constructor
            return [Task(task_id=task['id'], title=task['title'], completed=task['completed']) for task in tasks_data]
    return []

# Save tasks to a file (tasks.json)
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

# Add a new task
def add_task(tasks, title):
    task_id = 1 if not tasks else tasks[-1].id + 1  # Auto-increment task ID
    task = Task(task_id, title)  # Create new Task object
    tasks.append(task)  # Add the new task to the list
    save_tasks(tasks)  # Save the updated task list
    print(f"Task '{title}' added successfully.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = 'Completed' if task.completed else 'Incomplete'
            print(f"{task.id}: {task.title} - {status}")

# Delete a task by ID
def delete_task(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)  # Remove the task from the list
            save_tasks(tasks)  # Save the updated task list
            print(f"Task {task_id} deleted successfully.")
            return
    print(f"Task with ID {task_id} not found.")

# Mark a task as completed
def complete_task(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True  # Mark the task as completed
            save_tasks(tasks)  # Save the updated task list
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")

# CLI Menu
def menu():
    tasks = load_tasks()  # Load existing tasks from the file

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(tasks, task_id)
        elif choice == '5':
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu when the script is executed directly
if __name__ == "__main__":
    menu()
