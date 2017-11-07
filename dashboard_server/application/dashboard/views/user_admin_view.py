from flask_admin.contrib.mongoengine import ModelView
from flask_security import utils
from flask_security.core import current_user
from wtforms import PasswordField

from dashboard_server.application.repositories.mongo_repository import get_mongo_connection

db = get_mongo_connection()


class UserAdmin(ModelView):
    column_exclude_list = ('password',)

    form_excluded_columns = ('password',)

    column_auto_select_related = True

    def is_accessible(self):
        return current_user.has_role('admin')

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()

        form_class.password2 = PasswordField('New Password')
        return form_class

    def on_model_change(self, form, model, is_created):
        if len(model.password2):
            model.password = utils.hash_password(model.password2)


class RoleAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')
