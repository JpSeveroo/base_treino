from database.connection import get_connection
from entities.entity import Task


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

        def find_by_id(self, task_id):
            # Consultar pelo ID
            pass

        def update(self, task):
            # Atualizar
            pass

        def delete(self, task_id):
            # Excluir
            pass
