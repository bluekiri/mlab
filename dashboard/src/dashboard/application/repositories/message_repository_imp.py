# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import List

from dashboard.domain.entities.message import *
from dashboard.domain.repositories.messages_repository import MessageRepository


class MessageRepositoryImp(MessageRepository):
    def save_message(self, message: Message):
        message.save()

    def get_message_by_id(self, message_id: str):
        messages = Message.objects(pk=message_id)
        if messages is not None:
            return messages.first()
        return None

    def get_direct_message(self, user: User):
        messages = list(
            Message.objects(topic=Topic.direct_message.name, user=user.pk))
        for message in messages:
            message.icon = SubjectData[message.subject_data].value["icon"]
        return messages

    def set_message_as_read(self, message_id: str, current_user: User):
        messages = Message.objects(pk=message_id,
                                   read_by__nin=[current_user.pk])
        if messages:
            messages.update(push__read_by=current_user.pk, upsert=True)

    def get_messages_by_topics(self, topic_list) -> List[Message]:
        return list(Message.objects(topic__in=topic_list))

    def get_all_messages(self):
        return list(Message.objects())
