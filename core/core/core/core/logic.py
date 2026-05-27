from datetime import datetime
from .storage import load_tasks, save_tasks
from .exceptions import TaskNotFoundError

def add_task(text, filepath="tasks.json"):
    tasks = load_tasks(filepath)
    new_task = {"id": len(tasks) + 1, "text": text, "done": False, "created": datetime.now().isoformat()}
    tasks.append(new_task)
    save_tasks(tasks, filepath)
    return new_task

def complete_task(task_id, filepath="tasks.json"):
    tasks = load_tasks(filepath)
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks, filepath)
            return task
    raise TaskNotFoundError(f"Задача с ID {task_id} не найдена")

def list_tasks(filepath="tasks.json"):
    return load_tasks(filepath)
