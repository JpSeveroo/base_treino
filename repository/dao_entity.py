from database.connection import get_connection
from entities.entity import Task


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

    def find_by_id(self, task_id):
        # Consultar pelo ID
        pass

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass