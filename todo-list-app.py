import json
import os

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from file. Returns empty list if file doesn't exist."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("\n  No tasks found!")
        return

    print("\n  YOUR TASKS")
    print("  " + "-" * 30)
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        print(f"  {i}. [{status}] {task['text']}")
    print("  " + "-" * 30)

    done = sum(1 for t in tasks if t["done"])
    print(f"  {done}/{len(tasks)} completed\n")


def add_task(tasks):
    """Add a new task."""
    text = input("  Enter task: ").strip()
    if not text:
        print("  Task cannot be empty!")
        return
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"  Task added: '{text}'")


def complete_task(tasks):
    """Mark a task as complete."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"  Task {num} marked as complete!")
        else:
            print("  Invalid task number!")
    except ValueError:
        print("  Please enter a valid number!")


def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"  Deleted: '{removed['text']}'")
        else:
            print("  Invalid task number!")
    except ValueError:
        print("  Please enter a valid number!")


def show_menu():
    """Display the main menu."""
    print("\n  TO-DO LIST APP")
    print("  ==============")
    print("  1. View all tasks")
    print("  2. Add task")
    print("  3. Complete task")
    print("  4. Delete task")
    print("  5. Exit")


def main():
    """Main app loop."""
    tasks = load_tasks()
    print("\n  Welcome to your To-Do List!")

    while True:
        show_menu()
        choice = input("\n  Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n  Goodbye! Stay productive! 💪\n")
            break
        else:
            print("  Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()