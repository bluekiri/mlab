# coding: utf-8
from typing import List

from dashboard_server.domain.entities.auth.login_model import User
from dashboard_server.domain.entities.message import Message


class MessageRepository:
    def get_all_messages(self) -> List[Message]:
        raise NotImplementedError()

    def get_messages_by_topics(self, topic: List[str]) -> List[Message]:
        raise NotImplementedError()

    def set_message_as_read(self, message_id: str, current_user: User):
        raise NotImplementedError()

    def get_direct_message(self, user: User) -> Message:
        raise NotImplementedError()

    def get_message_by_id(self, message_id: str) -> Message:
        raise NotImplementedError()

    def save_message(self, message: Message):
        raise NotImplementedError()
