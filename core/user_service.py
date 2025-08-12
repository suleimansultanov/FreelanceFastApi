# app/core/user_service.py
from database.user_repo import UserRepository
from models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, username: str, password: str) -> User:
        hashed_password = pwd_context.hash(password)
        user = User(name=username, hashed_password=hashed_password)
        return self.user_repo.create(user)

    def authenticate(self, username: str, password: str):
        user = self.user_repo.get_by_username(username)
        if not user:
            return None
        if not pwd_context.verify(password, user.hashed_password):
            return None
        return user

    def search_users(self, query: str):
        return self.user_repo.search_by_name(query)
