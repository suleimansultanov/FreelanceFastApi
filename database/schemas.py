from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from enum import Enum
from datetime import date
from models.user import User


class TaskStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskCategory(str, Enum):
    CLEANING = "cleaning"
    DELIVERY = "delivery"
    writing = "writing"
    design = "design"
    education = "education" 
    other = "other"


class CategoryEnum(str, Enum):
    CLEANING = "cleaning"
    DELIVERY = "delivery"
    writing = "writing"
    design = "design"
    education = "education" 
    other = "other"

class StatusEnum(str, Enum):
    open = "open"
    in_progress = "in_progress"
    completed = "completed"

class TaskCreate(BaseModel):
    title: str
    description: str
    location: Optional[str]
    price: float
    startDate: datetime
    endDate: Optional[datetime]
    category: TaskCategory
    status: TaskStatus
    hasResponses: bool
    isRemote: bool

class TaskResponse(BaseModel):
    id: UUID
    title: str
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    category: CategoryEnum
    status: StatusEnum
    hasResponses: bool
    isRemote: bool
    price: float
    create_date: datetime
    description: str
    location: str

class TokenData(BaseModel):
    username: str | None = None

def convert_task_to_response(task_db_model) -> TaskResponse:
    return TaskResponse(
        id=task_db_model.id,
        title=task_db_model.title,
        startDate=task_db_model.start_date,
        endDate=task_db_model.end_date,
        category=task_db_model.category.lower(),  # convert to lowercase
        status=task_db_model.status.lower(),
        hasResponses=task_db_model.has_responses,
        isRemote=task_db_model.is_remote,
        price=task_db_model.price,
        create_date=task_db_model.create_date,
        location=task_db_model.location,
        description=task_db_model.description
        
    )


class MessageCreate(BaseModel):
    receiver_id: str
    content: str

class MessageResponse(BaseModel):
    id: str
    sender_id: str
    receiver_id: str
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True

def convert_user_to_response(user: User) -> UserResponse:
    return UserResponse.from_orm(user)