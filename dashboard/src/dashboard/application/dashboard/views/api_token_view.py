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

from uuid import uuid4

from flask_admin.contrib.mongoengine import ModelView
from flask_security.core import current_user

from dashboard.application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from dashboard.domain.entities.auth.api_token_model import Token


class ApiTokenView(ModelView, metaclass=ViewSecurityListeners):
    can_edit = False
    can_view = True
    can_create = False

    # Don't include the standard password field when creating or editing a User
    form_excluded_columns = ('token',)

    # Automatically display human-readable names for the current and
    # available Roles when creating or editing a User
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
