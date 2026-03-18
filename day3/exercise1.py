import argparse
import json
import os
from datetime import datetime

class Task:
    def __init__(self, id, title, status="todo", created_at=None):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at
        }

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return [Task(**task) for task in json.load(f)]
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Error: The tasks.json file is corrupted. {e}")
                return []
        return []

    def save_tasks(self):
        """ Save tasks to the tasks.json file. """
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title):
        """ Add a new task. """
        task_id = max([task.id for task in self.tasks], default=0) + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        self.save_tasks()

    def complete_task(self, task_id):
        """ Mark a task as 'done' by its id. """
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.status = 'done'
            self.save_tasks()
        else:
            print(f"Error: Task with id {task_id} not found.")

    def list_tasks(self, filter=None):
        """ List tasks, optionally filter by 'todo' or 'done' status. """
        tasks_to_list = self.tasks
        if filter:
            tasks_to_list = [t for t in self.tasks if t.status == filter]

        if not tasks_to_list:
            print(f"No tasks found for filter '{filter}'." if filter else "No tasks found.")
        else:
            for task in tasks_to_list:
                print(f"ID: {task.id}, Title: {task.title}, Status: {task.status}, Created at: {task.created_at}")

    def delete_task(self, task_id):
        """ Delete a task by its id. """
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
        else:
            print(f"Error: Task with id {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparser = parser.add_subparsers(dest="command")

    add_parser = subparser.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Title of the task")

    done_parser = subparser.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="ID of the task to mark as done")

    list_parser = subparser.add_parser("list", help="List all tasks")
    list_parser.add_argument("--filter", choices=["todo", "done"], help="Filter tasks by status")

    delete_parser = subparser.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")
    
    args = parser.parse_args()

    task_manager = TaskManager()
    
    if args.command == "add":
        task_manager.add_task(args.title)
    elif args.command == "done":
        task_manager.complete_task(args.id)
    elif args.command == "list":
        task_manager.list_tasks(args.filter)
    elif args.command == "delete":
        task_manager.delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()