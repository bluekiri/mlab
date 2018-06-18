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
