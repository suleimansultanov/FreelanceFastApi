# users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from database.schemas import UserResponse, convert_user_to_response
from auth.dependencies import get_db

router = APIRouter()

@router.get("/search", response_model=list[UserResponse])
def search_users(q: str, db: Session = Depends(get_db)):
    result = db.execute(select(User).filter(User.name.contains(q)).limit(20))
    users = result.scalars().all()
    return [convert_user_to_response(user) for user in users]
