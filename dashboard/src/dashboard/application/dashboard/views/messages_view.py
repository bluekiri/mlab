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

from flask import abort
from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required

from dashboard.domain.interactor.users.current_user import CurrentUser
from dashboard.domain.repositories.messages_repository import MessageRepository
from dashboard.domain.interactor.messages.user_messaging import UserMessaging


class MessageView(BaseView):
    def __init__(self, name, menu_icon_type, menu_icon_value, endpoint,
                 message_repository: MessageRepository,
                 user_messaging: UserMessaging, current_user: CurrentUser):
        super().__init__(name=name, menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value, endpoint=endpoint)
        self.current_user = current_user
        self.user_messaging = user_messaging
        self.message_repository = message_repository

    @login_required
    @expose('/')
    def index(self):
        user = self.current_user.get_current_user()
        messages = self.user_messaging.get_all_messages()
        for message in messages:
            message.is_read = user in message.read_by
        return self.render('messages/index.html', messages=messages)

    @login_required
    @expose('/<message_id>')
    def message(self, message_id):
        current_user = self.current_user.get_current_user()
        message = self.message_repository.get_message_by_id(message_id)
        if message is None:
            abort(404)
        # TODO check permission
        self.message_repository.set_message_as_read(message_id, current_user)
        return self.render('messages/details.html', message=message)
