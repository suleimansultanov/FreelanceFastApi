# app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.user_repo import UserRepository
from core.user_service import UserService
from fastapi.security import OAuth2PasswordRequestForm
from auth.dependencies import get_db
from auth.security import create_access_token

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return UserService(user_repo)

@router.post("/register")
def register(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(get_user_service)):
    existing_user = user_service.user_repo.get_by_username(form_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = user_service.create_user(form_data.username, form_data.password)
    return {"msg": "User created", "user_id": str(user.id)}

@router.post("/token")
def token(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(get_user_service)):
    user = user_service.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.name, "id": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
