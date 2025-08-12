from database.task_repo import TaskRepository
from models.task import Task
from uuid import UUID

class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    def get_tasks(self):
        return self.task_repo.get_all()

    def get_task(self, task_id: UUID):
        return self.task_repo.get_by_id(task_id)

    def create_task(self, task: Task):
        return self.task_repo.create(task)
