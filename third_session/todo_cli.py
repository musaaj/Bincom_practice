import cmd
from typing import List
from todolist import Task, TodoList


class TodoListCLI(cmd.Cmd):
    """
    Provides a command-line interface for managing a to-do list.

    Attributes:
        prompt (str): The prompt to display at the command prompt.
        todo_list (TodoList): The to-do list being managed.
    """

    prompt = "> "

    def __init__(self, todo_list: TodoList):
        super().__init__()
        self.todo_list = todo_list

    def do_add(self, arg: str) -> None:
        """Adds a new task to the to-do list."""
        self.todo_list.add_task(arg)
        print("Task added successfully.")

    def do_complete(self, arg: str) -> None:
        """Marks a task as completed."""
        try:
            task_id = int(arg)
        except ValueError:
            print("Invalid task ID.")
            return
        self.todo_list.complete_task(task_id)
        print("Task marked as completed.")

    def do_delete(self, arg: str) -> None:
        """Deletes a task from the to-do list."""
        try:
            task_id = int(arg)
        except ValueError:
            print("Invalid task ID.")
            return
        self.todo_list.delete_task(task_id)
        print("Task deleted successfully.")

    def do_list(self, arg: str) -> None:
        """Lists all tasks in the to-do list."""
        tasks = self.todo_list.get_tasks()
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            status = "completed" if task.completed else "not completed"
            print(f"{task.id}. {task.task} ({status})")

    def do_quit(self, arg: str) -> bool:
        """Quits the program."""
        return True


if __name__ == "__main__":
    todo_list = TodoList("localhost", "my_database", "musaaj", "tecnos9999$%")
    TodoListCLI(todo_list).cmdloop("Welcome to the to-do list manager!")

