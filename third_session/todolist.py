import psycopg2
from typing import List


class Task:
    """
    Represents a single task in the to-do list.

    Attributes:
        id (int): The unique identifier of the task.
        task (str): The description of the task.
        completed (bool): Whether the task has been completed.
    """

    def __init__(self, task_id: int, task: str, completed: bool):
        self.id = task_id
        self.task = task
        self.completed = completed


class TodoList:
    """
    Represents a to-do list that is stored in a PostgreSQL database.

    Attributes:
        conn (psycopg2.extensions.connection): The connection to the database.
        cur (psycopg2.extensions.cursor): The cursor used to execute SQL commands.
    """

    def __init__(self, db_host: str, db_name: str, db_user: str,
                 db_password: str) -> None:
        """
        Initializes a new TodoList object and connects to the database.

        Args:
            db_host (str): The hostname of the PostgreSQL server.
            db_name (str): The name of the database to use.
            db_user (str): The username to use for authentication.
            db_password (str): The password to use for authentication.
        """
        self.conn: psycopg2.extensions.connection = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )
        self.cur: psycopg2.extensions.cursor = self.conn.cursor()
        self._create_tasks_table()

    def _create_tasks_table(self) -> None:
        """
        Creates the tasks table if it doesn't already exist.
        """
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE
            );
            """
        )
        self.conn.commit()

    def add_task(self, task: str) -> None:
        """
        Adds a new task to the to-do list.

        Args:
            task (str): The description of the new task.
        """
        self.cur.execute(
            "INSERT INTO tasks (task) VALUES (%s);",
            (task,)
        )
        self.conn.commit()

    def complete_task(self, task_id: int) -> None:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.
        """
        self.cur.execute(
            "UPDATE tasks SET completed = TRUE WHERE id = %s;",
            (task_id,)
        )
        self.conn.commit()

    def delete_task(self, task_id: int) -> None:
        """
        Deletes a task from the to-do list.

        Args:
            task_id (int): The ID of the task to delete.
        """
        self.cur.execute(
            "DELETE FROM tasks WHERE id = %s;",
            (task_id,)
        )
        self.conn.commit()

    def get_tasks(self) -> List[Task]:
        """
        Retrieves all tasks from the database.

        Returns:
            list of Task: A list of Task objects
            representing the tasks in the to-do list.
        """
        self.cur.execute(
            "SELECT id, task, completed FROM tasks ORDER BY id;"
        )
        tasks = []
        for task in self.cur.fetchall():
            tasks.append(Task(*task))
        return tasks

    def __del__(self) -> None:
        """
        Closes the cursor and connection objects
        when the TodoList object is deleted.
        """
        self.cur.close()
        self.conn.close()

