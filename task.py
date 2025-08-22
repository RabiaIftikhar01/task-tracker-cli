#!/usr/bin/env python3
import sys
import json
from pathlib import Path

# File to store tasks (JSON format)
TASKS_FILE = Path("tasks.json")


def load_tasks():
    """Load tasks from file, return as list of dicts."""
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save tasks list to file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "desc": description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description} ✅")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. 🎉")
        return
    for task in tasks:
        status = "✅ Done" if task["done"] else "❌ Pending"
        print(f"""{task['id']}. {task['desc']} [{status}]""")


def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task #{task_id} marked as complete ✅")
            return
    print(f"No task found with id {task_id}")


def show_help():
    print("""
Usage: python task.py [command] [arguments]

Commands:
  add "description"   Add a new task
  list                List all tasks
  done ID             Mark task with given ID as done
  help                Show this help message
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Task description required")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        list_tasks()
    elif command == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Error: Task ID required")
            return
        mark_done(int(sys.argv[2]))
    else:
        show_help()


if __name__ == "__main__":
    main()
