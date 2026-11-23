from database.connection import get_connection
from entities.entity import Task
from contextlib import closing


class DAOEntity:

    def create(self, task: Task) -> Task:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO tasks (title, description) VALUES (?, ?)"
        valores = (task.title, task.description)
        cursor.execute(sql, valores)
        conn.commit()
        task.id = cursor.lastrowid
        conn.close()
        return task

    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM tasks"
        cursor.execute(sql)
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = Task(
                id=row["id"], title=row["title"], description=row["description"]
            )
            tasks.append(task)
                
        conn.close()
        return tasks

    def find_by_id(self, task_id: int) -> Task | None:
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
            task_info = cursor.fetchone()
            
            if not task_info:
                return None
            
            task = Task(task_info[1], task_info[2], task_info[0], task_info[3])
            return task

    def delete(self, task_id: int) -> int:
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            conn.commit()
            return cursor.rowcount
            
