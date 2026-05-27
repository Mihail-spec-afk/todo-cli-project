import argparse
import sys
from core.logic import add_task, complete_task, list_tasks
from core.exceptions import TodoError

def main():
    parser = argparse.ArgumentParser(description="CLI утилита для управления задачами")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="Показать все задачи")
    
    add_p = subparsers.add_parser("add", help="Добавить задачу")
    add_p.add_argument("text", help="Текст задачи")
    
    done_p = subparsers.add_parser("done", help="Отметить задачу выполненной")
    done_p.add_argument("id", type=int, help="ID задачи")

    args = parser.parse_args()

    try:
        if args.command == "list":
            tasks = list_tasks()
            if not tasks:
                print("Список задач пуст.")
            for t in tasks:
                status = "✅" if t["done"] else "⬜"
                print(f"{status} [{t['id']}] {t['text']}")
        elif args.command == "add":
            new = add_task(args.text)
            print(f"✅ Задача добавлена: [{new['id']}] {new['text']}")
        elif args.command == "done":
            completed = complete_task(args.id)
            print(f"✅ Задача отмечена выполненной: [{completed['id']}] {completed['text']}")
        else:
            parser.print_help()
    except TodoError as e:
        print(f"❌ Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
