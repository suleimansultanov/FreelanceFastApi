# tasks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from datetime import datetime
from models.task import Task
from database.schemas import TaskResponse, TaskCreate, convert_task_to_response
from auth.dependencies import get_db, get_current_user

router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    taskslist = [convert_task_to_response(task) for task in tasks]
    tasks_sorted = sorted(taskslist, key=lambda task: task.create_date, reverse=True)
    return tasks_sorted

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_task = Task(
        id=uuid4(),
        title=task.title,
        description=task.description,
        location=task.location,
        price=task.price,
        start_date=task.startDate,
        end_date=task.endDate,
        category=task.category,
        status=task.status,
        has_responses=task.hasResponses,
        is_remote=task.isRemote,
        user_id=current_user.id,
        create_date=datetime.now()
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return convert_task_to_response(new_task)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: UUID, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return convert_task_to_response(task)
