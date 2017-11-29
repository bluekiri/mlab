# coding: utf-8
from flask import abort
from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required

from dashboard_server.domain.interactor.users.current_user import CurrentUser
from dashboard_server.domain.repositories.messages_repository import MessageRepository
from domain.interactor.messages.user_messaging import UserMessaging


class MessageView(BaseView):
    def __init__(self, name, menu_icon_type, menu_icon_value, endpoint,
                 message_repository: MessageRepository, user_messaging: UserMessaging,
                 current_user: CurrentUser):
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
