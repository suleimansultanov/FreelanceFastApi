# models.py
from sqlalchemy import Column, String, Integer, Boolean, Date, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import uuid

Base = declarative_base()

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

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    category = Column(String, nullable=False)  # or Enum if you prefer
    status = Column(String, nullable=False)    # or Enum if you prefer
    has_responses = Column(Boolean, default=False)
    is_remote = Column(Boolean, default=False)
    create_date = Column(DateTime, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship("User", backref="tasks")

