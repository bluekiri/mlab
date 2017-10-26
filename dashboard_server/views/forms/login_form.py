import logging

from flask_security import LoginForm
from flask_security.utils import get_message
from wtforms import fields, validators

from dashboard_server.interactor.login.login_verification import is_success_pwd, \
    get_user_from_username


class CustomLoginForm(LoginForm):
    email = fields.StringField('username', validators=[validators.required()])
    password = fields.PasswordField('password', validators=[validators.required()])
    user = None

    def add_error_to_wtf_field(self, field, error_message):
        field.errors = list(field.errors)
        field.errors.append(error_message)

    def validate(self):
        user = get_user_from_username(self.email.data)
        self.user = user
        if self.user is None:
            self.add_error_to_wtf_field(self.email, get_message('USER_DOES_NOT_EXIST')[0])
            return False
        if not self.password.data:
            self.add_error_to_wtf_field(self.password, get_message('PASSWORD_NOT_SET')[0])
            return False
        if not is_success_pwd(self.email.data, self.password.data):
            self.add_error_to_wtf_field(self.password, get_message('INVALID_PASSWORD')[0])
            return False
        if not self.user.is_active:
            self.add_error_to_wtf_field(self.email, get_message('DISABLED_ACCOUNT')[0])
            return False
        logging.debug("Saving user %s" % user.email)
        user.save()
        return True

    def get_user(self):
        return self.user
