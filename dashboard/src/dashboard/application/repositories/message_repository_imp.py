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
