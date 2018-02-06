import logging

from flask_security import LoginForm, utils
from flask_security.utils import get_message
from wtforms import fields, validators

from dashboard_server.application.interactor.users.login_verification import get_user_from_username, \
    is_success_pwd
from dashboard_server.domain.entities.message import Message, SubjectData, Topic


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
        elif self.user.password is not None and utils.verify_password(self.password.data,
                                                                      self.user.password):
            return True
        if not self.password.data:
            self.add_error_to_wtf_field(self.password, get_message('PASSWORD_NOT_SET')[0])
            return False
        if not is_success_pwd(self.email.data, self.password.data):
            self.add_error_to_wtf_field(self.password, get_message('INVALID_PASSWORD')[0])
            return False
        if not self.user.is_active:
            self.add_error_to_wtf_field(self.email, get_message('DISABLED_ACCOUNT')[0])
            return False
        logging.debug("Saving or updating user %s" % user.email)
        # TODO this method have to much responsability... the validation name means validate form...
        user.save()
        self._send_welcome_message()
        return True

    def _send_welcome_message(self):
        # TODO this need be abstracted in a interactor but the flask security plugin throw a error...
        Message(user=self.get_user(), subject_data=SubjectData.welcome.name, text="",
                topic=Topic.direct_message.name,
                subject=SubjectData.welcome.value['text'] % self.get_user().name).save()

    def get_user(self):
        return self.user