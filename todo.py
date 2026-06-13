import json
import os
import sys
from datetime import datetime

TODO_FILE = "todos.json"


def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(title):
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().isoformat(),
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✅ Task added: [{todo['id']}] {title}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("📭 No tasks yet. Add one with: python todo.py add <task>")
        return
    print("\n📋 Your Todo List:")
    print("-" * 40)
    for t in todos:
        status = "✅" if t["done"] else "⬜"
        print(f"  {status} [{t['id']}] {t['title']}")
    print("-" * 40)
    done = sum(1 for t in todos if t["done"])
    print(f"  {done}/{len(todos)} completed\n")


def complete_todo(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save_todos(todos)
            print(f"🎉 Completed: [{t['id']}] {t['title']}")
            return
    print(f"❌ Task #{todo_id} not found.")


def delete_todo(todo_id):
    todos = load_todos()
    new_todos = [t for t in todos if t["id"] != todo_id]
    if len(new_todos) == len(todos):
        print(f"❌ Task #{todo_id} not found.")
        return
    save_todos(new_todos)
    print(f"🗑️  Deleted task #{todo_id}")


def print_help():
    print("""
🗒️  CLI Todo Tool — Usage:

  python todo.py add <task>      Add a new task
  python todo.py list            List all tasks
  python todo.py done <id>       Mark a task as completed
  python todo.py delete <id>     Delete a task
  python todo.py help            Show this help message
""")


def main():
    args = sys.argv[1:]
    if not args or args[0] == "help":
        print_help()
    elif args[0] == "add":
        if len(args) < 2:
            print("Usage: python todo.py add <task title>")
        else:
            add_todo(" ".join(args[1:]))
    elif args[0] == "list":
        list_todos()
    elif args[0] == "done":
        if len(args) < 2:
            print("Usage: python todo.py done <id>")
        else:
            complete_todo(int(args[1]))
    elif args[0] == "delete":
        if len(args) < 2:
            print("Usage: python todo.py delete <id>")
        else:
            delete_todo(int(args[1]))
    else:
        print(f"Unknown command: {args[0]}")
        print_help()


if __name__ == "__main__":
    main()
