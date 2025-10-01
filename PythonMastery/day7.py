# To-Do List CLI App (save tasks in file).
# 1. Add Task
# 2. View Tasks
# 3. Mark Task as Done
# 4. Exit
import os

FILENAME = "todo.txt"
def load_tasks():
    """Load tasks from file"""
    if(not os.path.exists(FILENAME)):
        return []
    with open(FILENAME, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    """Save tasks to file"""
    with open(FILENAME, 'w') as f:
        for task in tasks:
            f.write(task+"\n")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    print("\nYour tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
    print()

def add_tasks(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!\n")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark done: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' marked as done!\n")
        else:
            print("Invalid task number\n")
    except ValueError:
        print("Please enter a number. \n")


def todo_cli():
    tasks = load_tasks()

    while True:
        print("1. Add\n2. View\n3. Mark Task as Done\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")
    

# Contact Book (CRUD operations with dictionary).

# Quiz Game (random Q&A + scoring).

# Weather App (use requests to fetch JSON).

# Password Generator (random, secure).

# Bonus Challenges (Day 7):

# Build a calculator app.

# Build a simple login system with file-based user storage.

# Create a random password generator.

# Scrape website titles with requests + BeautifulSoup.

# Create a student management system (OOP + files).

def main():
    todo_cli()

if __name__ == "__main__":
    main()