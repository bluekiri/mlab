# coding: utf-8
from typing import List

from domain.entities.message import *
from domain.repositories.messages_repository import MessageRepository


class MessageRepositoryImp(MessageRepository):
    def save_message(self, message: Message):
        message.save()

    def get_message_by_id(self, message_id: str):
        messages = Message.objects(pk=message_id)
        if messages is not None:
            return messages.first()
        return None

    def get_direct_message(self, user: User):
        messages = list(Message.objects(topic=Topic.direct_message.name, user=user.pk))
        for message in messages:
            message.icon = SubjectData[message.subject_data].value["icon"]
        return messages

    def set_message_as_read(self, message_id: str, current_user: User):
        messages = Message.objects(pk=message_id, read_by__nin=[current_user.pk])
        if messages:
            messages.update(push__read_by=current_user.pk, upsert=True)

    def get_messages_by_topics(self, topic_list) -> List[Message]:
        return list(Message.objects(topic__in=topic_list))

    def get_all_messages(self):
        return list(Message.objects())
