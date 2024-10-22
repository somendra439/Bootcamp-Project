import json

class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        return f"Title: {self.title}, Priority: {self.priority}, Due Date: {self.due_date}, Completed: {self.completed}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' removed.")
        else:
            print("Invalid task index.")

    def mark_task_as_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task '{self.tasks[index].title}' marked as complete.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)
        print(f"Tasks saved to {filename}.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks = json.load(file)
                self.tasks = [Task(**task) for task in tasks]
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print(f"No file named {filename} found.")

def to_do_list_app():
    todo_list = ToDoList()
    todo_list.load_tasks('tasks.json')

    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. Display All Tasks")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter task priority: ")
            due_date = input("Enter task due date: ")
            todo_list.add_task(title, priority, due_date)
        elif choice == "2":
            index = int(input("Enter task index to remove: "))
            todo_list.remove_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as complete: "))
            todo_list.mark_task_as_complete(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            todo_list.save_tasks('tasks.json')
        elif choice == "6":
            todo_list.save_tasks('tasks.json')
            break
        else:
            print("Invalid option. Please try again.")

# Run the to-do list app
to_do_list_app()
