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


from dashboard.domain.entities.auth.login_model import User
from dashboard.domain.interactor.users.login_verification import \
    LoginVerification
from dashboard.domain.repositories.ldap_repository import LdapRepository
from dashboard.domain.repositories.mongo_security_repository import \
    MongoSecurityRepository


class LoginVerificationImp(LoginVerification):
    def __init__(self, mongo_security_repository: MongoSecurityRepository,
                 ldap_repository: LdapRepository):
        self.ldap_repository = ldap_repository
        self.mongo_security_repository = mongo_security_repository

    def is_success_pwd(self, username, pwd):
        return self.ldap_repository.is_correct_pwd(username=username, pwd=pwd)

    def get_user_from_email(self, email) -> User:
        user = self.mongo_security_repository.get_user_from_email(email)
        if user is not None:
            return user

        # Get user from ldap
        user_entry = self.ldap_repository.get_user_by_username_info(
            username=email)
        if user_entry is not None:

            return User(name=str(user_entry.name),
                        username=str(user_entry.mail).split('@')[0],
                        email=str(user_entry.mail))
