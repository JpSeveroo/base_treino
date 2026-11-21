import sqlite3


class TaskRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def create(self, task: Task) -> Task:
        cursor = self.connection.cursor()
        cursor.execute(
            """INSERT INTO tasks (title, description) VALUES (?,?)""",
            (task.title, task.description),
        )
        self.connection.commit()

        # É o seguinte, como a entidade não possui um id definido de inicio
        # o banco iria atribuir o id disponivel mas apenas para dentro do banco,
        # com isso aqui a gente grava no atributo .id
        task.id = connection.lastrowid
        return task
