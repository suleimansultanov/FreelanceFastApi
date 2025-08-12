from sqlalchemy import create_engine, Column, String, Boolean, Date, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import uuid
from datetime import datetime
from .base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    category = Column(String, nullable=False)
    status = Column(String, nullable=False)
    has_responses = Column(Boolean, default=False)
    is_remote = Column(Boolean, default=False)
    create_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="tasks")
