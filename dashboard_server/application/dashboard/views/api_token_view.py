from uuid import uuid4

from flask_admin.contrib.mongoengine import ModelView
from flask_security.core import current_user

# from web_service.dashboard.views.util.view_roles_management import ViewSecurityListeners
# from web_service.models.auth.api_token_model import Token
from application.dashboard.views.util.view_roles_management import ViewSecurityListeners


class ApiTokenView(ModelView, metaclass=ViewSecurityListeners):
    can_edit = False
    can_view = True
    can_create = False

    # Don't include the standard password field when creating or editing a User
    form_excluded_columns = ('token',)

    # Automatically display human-readable names for the current and available Roles when creating or editing a User
    column_auto_select_related = True

    def is_accessible(self):
        return current_user.is_authenticated

    def has_edit_role(self):
        self.can_edit = True

    def has_admin_role(self):
        self.can_edit = True
        self.can_create = True

    def generate_auth_token(self):
        new_token = uuid4()
        t = Token.objects(token=new_token)
        if t:
            raise NotImplementedError

        return new_token

    def _on_model_change(self, form, model, is_created):
        token = self.generate_auth_token()
        model.token = str(token)