from sqlalchemy.orm import Session
from models import task
from uuid import UUID

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(task).all()

    def get_by_id(self, task_id: UUID):
        return self.db.query(task).filter(task.id == task_id).first()

    def create(self, task: task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task
