from entities.entity import Task

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, title: str, description: str = "") -> Task:
        if not title or not title.strip():
          raise ValueError(
              "O título da tarefa é obrigatório e não pode conter apenas espaços."
          )

        clean_title = title.strip()
        clean_description = description.strip() if description else ""

        new_task = Task(title=clean_title, description=clean_description)

        return self.repository.create(new_task)

    def list(self):
        pass

    def get(self, task_id: int) -> Task:
        if not isinstance(task_id, int):
            raise ValueError(f"Digite um número.")
        task = self.repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Task com id {task_id} não existe")
        return task
        
    def update(self, task_id: int, title: str, description: str = "") -> None:
        if not title or not title.strip():
            raise ValueError(
                "O título da tarefa é obrigatório e não pode conter apenas espaços."
            )

        task = self.get(task_id)
        task.title = title.strip()
        task.description = description.strip() if description else ""

        if not self.repository.update(task):
            raise ValueError(f"Task com id {task_id} não existe")
    
    def delete(self, task_id):
        delete = self.repository.delete(task_id)
        if not delete:
            raise ValueError(f"Task com id {task_id} não existe")

    def complete(self, task_id: int) -> bool:
        return self._change_status(task_id, completed=True)
    
    def reopen(self, task_id: int) -> bool:
        return self._change_status(task_id, completed=False)

    def _change_status(self, task_id: int, completed: bool):
        self.get(task_id)
        if self.repository.set_completed(task_id, completed):
            return True

        self.get(task_id)
        return False