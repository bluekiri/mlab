# coding:utf-8
from typing import List

from dashboard_server.domain.entities.message import Message


class UserMessaging:
    def get_pending_messages(self) -> List[Message]:
        raise NotImplementedError()

    def set_message_as_read(self, message_id: str):
        raise NotImplementedError()
