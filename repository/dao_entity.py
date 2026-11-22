from database.connection import get_connection
from entities.entity import Task
from contextlib import closing


class DAOEntity:

    def create(self, task: Task) -> Task:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (task.title, task.description),
        )
        conn.commit()

        task.id = cursor.lastrowid
        conn.close()
        return task

    def find_all(self):
        # Consultar todas as entidades
        pass

    def find_by_id(self, task_id: int) -> Task | None:
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
            task_info = cursor.fetchone()
            
            if not task_info:
                return None
            
            task = Task(task_info[1], task_info[2], task_info[0], task_info[3])
            return task

    def update(self, task):
        with closing(get_connection()) as conn:
            cursor = conn.execute(
                """
                UPDATE tasks
                SET title = ?, description = ?
                WHERE id = ?
                """,
                (task.title, task.description, task.id)
            )
            conn.commit()
            return cursor.rowcount == 1

    def delete(self, task_id):
        # Excluir
        pass