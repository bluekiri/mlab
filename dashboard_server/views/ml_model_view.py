from flask_admin.contrib.mongoengine import ModelView
from flask_security.core import current_user

from dashboard_server.views.util.view_roles_management import ViewSecurityListeners


class MlModelView(ModelView, metaclass=ViewSecurityListeners):
    can_edit = False
    can_view = True
    can_create = False


    def is_accessible(self):
        return current_user.is_authenticated

    def has_edit_role(self):
        self.can_edit = True

    def has_admin_role(self):
        self.can_edit = True
        self.can_create = True
