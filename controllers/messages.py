# messages.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import uuid4
from datetime import datetime
from models.message import Message
from database.schemas import MessageCreate, MessageResponse
from auth.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/send", response_model=MessageResponse)
async def send_message(
    message: MessageCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_message = Message(
        id=uuid4(),
        sender_id=current_user.id,
        receiver_id=message.receiver_id,
        content=message.content,
        timestamp=datetime.utcnow()
    )
    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)
    return new_message

@router.get("/{receiver_id}", response_model=list[MessageResponse])
async def get_conversation(
    receiver_id: str,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = await db.execute(
        select(Message).filter(
            ((Message.sender_id == current_user.id) & (Message.receiver_id == receiver_id)) |
            ((Message.sender_id == receiver_id) & (Message.receiver_id == current_user.id))
        ).order_by(Message.timestamp)
    )
    return result.scalars().all()
