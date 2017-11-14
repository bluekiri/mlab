# coding: utf-8
import datetime
from typing import List

from dashboard_server.domain.entities.message import Message
from dashboard_server.domain.interactor.users.current_user import CurrentUser
from dashboard_server.domain.interactor.users.user_messaging import UserMessaging


class UserMessagingImp(UserMessaging):
    def __init__(self, current_user: CurrentUser):
        self.current_user = current_user

    def get_pending_messages(self) -> List[Message]:
        # user = self.current_user.get_current_user()
        message1 = Message()
        message1.subject = "Subject"
        message1.ts = datetime.datetime.utcnow()
        message1.text = "Lorem fistrum fistro ese pedazo de papaar papaar pupita hasta luego Lucas condemor al ataquerl."
        messages = [message1, message1, message1, message1]
        return []

    def set_message_as_read(self, message_id: str):
        pass
