import argparse
import json
from datetime import datetime
from pathlib import Path


DATA_DIRECTORY = Path("/data")
DATA_FILE = DATA_DIRECTORY / "tasks.json"


def ensure_data_directory():
    DATA_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )


def load_tasks():
    ensure_data_directory()

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except (
        json.JSONDecodeError,
        OSError
    ):
        return []


def save_tasks(tasks):
    ensure_data_directory()

    with DATA_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            tasks,
            file,
            indent=4
        )


def get_next_id(tasks):
    if not tasks:
        return 1

    return max(
        task["id"]
        for task in tasks
    ) + 1


def add_task(title):
    tasks = load_tasks()

    task = {
        "id": get_next_id(tasks),
        "title": title,
        "completed": False,
        "created": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )
    }

    tasks.append(task)

    save_tasks(tasks)

    print()
    print("=" * 55)
    print("StudyTrack - Task Added")
    print("=" * 55)

    print(
        f'ID: {task["id"]}'
    )

    print(
        f'Task: {task["title"]}'
    )

    print(
        f'Created: {task["created"]}'
    )

    print("=" * 55)


def list_tasks():
    tasks = load_tasks()

    print()
    print("=" * 65)
    print("StudyTrack - Study Tasks")
    print("=" * 65)

    if not tasks:
        print(
            "No study tasks have been added yet."
        )

        print("=" * 65)
        return

    for task in tasks:

        if task["completed"]:
            status = "DONE"
        else:
            status = "TODO"

        print(
            f'{task["id"]:>2}. '
            f'[{status}] '
            f'{task["title"]}'
        )

        print(
            f'    Created: '
            f'{task["created"]}'
        )

    print("=" * 65)


def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:

            if task["completed"]:
                print(
                    f"Task {task_id} is already completed."
                )

                return

            task["completed"] = True

            save_tasks(tasks)

            print()
            print("=" * 55)
            print("StudyTrack - Task Completed")
            print("=" * 55)

            print(
                f'Task {task_id}: '
                f'{task["title"]}'
            )

            print(
                "Status: DONE"
            )

            print("=" * 55)

            return

    print(
        f"Task {task_id} was not found."
    )


def show_stats():
    tasks = load_tasks()

    total = len(tasks)

    completed = sum(
        1
        for task in tasks
        if task["completed"]
    )

    remaining = total - completed

    if total == 0:
        percentage = 0
    else:
        percentage = round(
            (completed / total) * 100
        )

    print()
    print("=" * 55)
    print("StudyTrack - Progress Summary")
    print("=" * 55)

    print(
        f"Total tasks:      {total}"
    )

    print(
        f"Completed:        {completed}"
    )

    print(
        f"Remaining:        {remaining}"
    )

    print(
        f"Progress:         {percentage}%"
    )

    print("=" * 55)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "StudyTrack - "
            "Docker command-line study task manager"
        )
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )


    add_parser = subparsers.add_parser(
        "add",
        help="Add a study task"
    )

    add_parser.add_argument(
        "title",
        help="Description of the study task"
    )


    subparsers.add_parser(
        "list",
        help="Display saved tasks"
    )


    done_parser = subparsers.add_parser(
        "done",
        help="Mark a task as completed"
    )

    done_parser.add_argument(
        "id",
        type=int,
        help="Task ID"
    )


    subparsers.add_parser(
        "stats",
        help="Display progress statistics"
    )


    args = parser.parse_args()


    if args.command == "add":
        add_task(
            args.title
        )

    elif args.command == "list":
        list_tasks()

    elif args.command == "done":
        complete_task(
            args.id
        )

    elif args.command == "stats":
        show_stats()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()