# coding: utf-8
from flask import abort
from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required

from dashboard_server.domain.repositories.messages_repository import MessageRepository


class MessageView(BaseView):
    def __init__(self, name, menu_icon_type, menu_icon_value, endpoint,
                 message_repository: MessageRepository):
        super().__init__(name=name, menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value, endpoint=endpoint)
        self.message_repository = message_repository

    @login_required
    @expose('/')
    def index(self):
        return self.render('messages/index.html')

    @login_required
    @expose('/message/<message_id>')
    def message(self, message_id):
        message = self.message_repository.get_message_by_id(message_id)
        if message is None:
            abort(404)
        # TODO check permission

        return self.render('messages/view.html')
