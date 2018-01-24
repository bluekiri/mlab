# coding: utf-8
from flask_admin.contrib.mongoengine import ModelView

from dashboard_server.domain.interactor.users.current_user import CurrentUser


class LogsView(ModelView):
    can_edit = False
    can_create = False
    can_delete = False

    def __init__(self, model, current_user: CurrentUser, name, menu_icon_type, menu_icon_value):
        super().__init__(model, name=name, menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self.current_user = current_user

    def is_accessible(self):
        return self.current_user.get_current_user().has_role('admin')
