# coding: utf-8
from typing import List

from dashboard_server.domain.entities.auth.login_model import User
from dashboard_server.domain.entities.message import Message


class MessageRepository:
    def get_all_messages(self):
        raise NotImplementedError()

    def get_messages_by_topic(self, topic: List[str]) -> List[Message]:
        raise NotImplementedError()

    def set_message_as_read(self, message_id: str, current_user: User):
        raise NotImplementedError()

    def get_direct_message(self, user: User):
        raise NotImplementedError()

    def get_message_by_id(self, message_id: str):
        raise NotImplementedError()
