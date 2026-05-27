import json
import os
from .exceptions import StorageError

def load_tasks(filepath="tasks.json"):
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise StorageError(f"Ошибка чтения файла: {e}")

def save_tasks(tasks, filepath="tasks.json"):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise StorageError(f"Ошибка записи файла: {e}")
