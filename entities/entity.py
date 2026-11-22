class Task:

  def __init__(self, title, description="", id=None, completed=0):
    self.id = id
    self.title = title
    self.description = description
    self.completed = completed
