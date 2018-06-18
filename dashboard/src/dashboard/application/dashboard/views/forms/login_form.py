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

import logging

from flask_security import LoginForm, utils
from flask_security.utils import get_message
from wtforms import fields, validators

from dashboard.application.interactor.users.login_verification_imp import \
    LoginVerificationImp
from dashboard.application.repositories.ldap_repository import LdapRepositoryImp
from dashboard.application.repositories.mongo_security_repository_imp import \
    MongoSecurityRepositoryImp
from dashboard.domain.entities.message import Message, SubjectData, Topic


class CustomLoginForm(LoginForm):
    email = fields.StringField('username', validators=[validators.required()])
    password = fields.PasswordField('password',
                                    validators=[validators.required()])
    user = None

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.ldap_repository = LdapRepositoryImp()
        self.mongo_security_repository = MongoSecurityRepositoryImp()
        self.login_verification = LoginVerificationImp(
            self.mongo_security_repository, self.ldap_repository)

    def add_error_to_wtf_field(self, field, error_message):
        field.errors = list(field.errors)
        field.errors.append(error_message)

    def validate(self):

        if not self.email.data or self.email.data.strip() == '':
            self.email.errors.append(get_message('EMAIL_NOT_PROVIDED')[0])
            return False

        if not self.password.data:
            self.add_error_to_wtf_field(self.password,
                                        get_message('PASSWORD_NOT_SET')[0])
            return False

        user = self.login_verification.get_user_from_email(
            self.email.data)
        self.user = user

        if self.user is not None:
            if not self.user.is_active:
                self.add_error_to_wtf_field(self.email,
                                            get_message('DISABLED_ACCOUNT')[0])
                return False

            if self.user.password is not None and utils.verify_password(
                    self.password.data, self.user.password):
                return True
            elif self.user.password is None and self.login_verification.is_success_pwd(
                    self.user.email, self.password.data):
                return True
            else:
                self.add_error_to_wtf_field(self.email,
                                            get_message('INVALID_PASSWORD')[
                                                0])
                return False

        else:
            self.add_error_to_wtf_field(self.email,
                                        get_message('USER_DOES_NOT_EXIST')[
                                            0])
            return False

    def _send_welcome_message(self):
        # TODO this need be abstracted in a interactor but the flask security plugin throw a error...
        messages = Message.objects(user=self.get_user(),
                                   subject_data=SubjectData.welcome.name)
        if len(messages) == 0:
            Message(user=self.get_user(), subject_data=SubjectData.welcome.name,
                    text="",
                    topic=Topic.direct_message.name,
                    subject=SubjectData.welcome.value[
                                'text'] % self.get_user().name).save()

    def get_user(self):
        return self.user
