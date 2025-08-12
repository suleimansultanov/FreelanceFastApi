from database.messages_repo import MessageRepository
from models.message import Message

class MessageService:
    def __init__(self, message_repo: MessageRepository):
        self.message_repo = message_repo

    def send_message(self, message: Message):
        return self.message_repo.create(message)

    def get_conversation(self, sender_id: str, receiver_id: str):
        return self.message_repo.get_conversation(sender_id, receiver_id)
