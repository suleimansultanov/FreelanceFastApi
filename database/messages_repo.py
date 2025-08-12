from sqlalchemy.orm import Session
from models.message import Message
from sqlalchemy import select, or_
from uuid import UUID

class MessageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, message: Message):
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_conversation(self, sender_id: str, receiver_id: str):
        return self.db.execute(
            select(Message).filter(
                ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
                ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
            ).order_by(Message.timestamp)
        ).scalars().all()
