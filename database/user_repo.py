# app/db/user_repo.py
from sqlalchemy.orm import Session
from models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.name == username).first()

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def search_by_name(self, query: str, limit: int = 20):
        return self.db.query(User).filter(User.name.contains(query)).limit(limit).all()

