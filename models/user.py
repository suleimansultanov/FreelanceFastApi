# models.py
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import uuid
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    avatar_url = Column(String, nullable=True)
    balance = Column(Float, default=0.0)
    tasks_created = Column(Integer, default=0)
    tasks_completed = Column(Integer, default=0)
    is_verified = Column(Boolean, default=False)
    rating = Column(Float, nullable=True)

    tasks = relationship("Task", back_populates="user")  # обратная связь
