# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Bluekiri V5 BigData Team <bigdata@bluekiri.com>.
#
# This program is free software: you can redistribute it and/or  modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# As a special exception, the copyright holders give permission to link the
# code of portions of this program with the OpenSSL library under certain
# conditions as described in each individual source file and distribute
# linked combinations including the program with the OpenSSL library. You
# must comply with the GNU Affero General Public License in all respects for
# all of the code used other than as permitted herein. If you modify file(s)
# with this exception, you may extend this exception to your version of the
# file(s), but you are not obligated to do so. If you do not wish to do so,
# delete this exception statement from your version. If you delete this
# exception statement from all source files in the program, then also delete
# it in the license file.

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
