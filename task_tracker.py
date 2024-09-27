import sys
import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = 'tasks.json'

# Load tasks from JSON file or create the file if it doesn't exist
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

# List all tasks
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"{task['id']}. {task['description']} [{task['status']}]")

# Handle user input
def handle_input(args):
    if args[0] == 'add':
        add_task(' '.join(args[1:]))
    elif args[0] == 'list':
        if len(args) > 1:
            list_tasks(args[1])
        else:
            list_tasks()
    # More commands like update, delete, mark-in-progress, etc., will be added here

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
    else:
        handle_input(sys.argv[1:])
