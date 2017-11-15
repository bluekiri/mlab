# coding: utf-8
from typing import List

from dashboard_server.domain.entities.message import Message
from dashboard_server.domain.interactor.users.current_user import CurrentUser
from dashboard_server.domain.interactor.users.user_messaging import UserMessaging
from dashboard_server.domain.repositories.messages_repository import MessageRepository


class UserMessagingImp(UserMessaging):
    def __init__(self, current_user: CurrentUser, message_repository: MessageRepository):
        self.message_repository = message_repository
        self.current_user = current_user

    def get_pending_messages(self) -> List[Message]:
        user = self.current_user.get_current_user()
        direct_messages = self.message_repository.get_direct_message(user)
        return direct_messages + self.message_repository.get_messages_by_topic(user.topics)

    def set_message_as_read(self, message_id: str):
        self.message_repository.set_message_as_read(message_id,
                                                    self.current_user.get_current_user())
