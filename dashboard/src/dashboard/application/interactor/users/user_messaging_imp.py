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

from dashboard.domain.entities.message import Message
from dashboard.domain.interactor.messages.user_messaging import UserMessaging
from dashboard.domain.interactor.users.current_user import CurrentUser
from dashboard.domain.repositories.messages_repository import MessageRepository


class UserMessagingImp(UserMessaging):
    def __init__(self, current_user: CurrentUser, message_repository: MessageRepository):
        self.message_repository = message_repository
        self.current_user = current_user

    def get_pending_messages(self) -> List[Message]:
        user = self.current_user.get_current_user()
        direct_messages = self.message_repository.get_direct_message(user)
        messages = direct_messages + self.message_repository.get_messages_by_topics(user.topics)
        return [message for message in messages if user not in message.read_by]

    def set_message_as_read(self, message_id: str):
        self.message_repository.set_message_as_read(message_id,
                                                    self.current_user.get_current_user())

    def get_all_messages(self):
        current_user = self.current_user.get_current_user()
        topics = current_user.topics
        direct_messages = self.message_repository.get_direct_message(current_user)
        topics_messages = self.message_repository.get_messages_by_topics(topics)
        all_messages = direct_messages + topics_messages
        all_messages.sort(key=lambda item: item.ts)
        return all_messages
