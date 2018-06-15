# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from flask_admin.contrib.mongoengine import ModelView
from flask_security import utils
from flask_security.core import current_user
from wtforms import PasswordField, SelectMultipleField

from dashboard.application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from dashboard.domain.entities.message import Topic


class UserAdmin(ModelView, metaclass=ViewSecurityListeners):
    can_edit = False
    can_delete = False
    can_create = False
    column_exclude_list = ('password',)

    form_excluded_columns = ('password',)

    column_auto_select_related = True
    edit_template = 'security/user.html'

    form_widget_args = {
        'topics': {
            'readonly': True
        },
    }

    def has_admin_role(self):
        self.can_edit = True
        self.can_delete = True
        self.can_create = True

    def is_accessible(self):
        return current_user.has_role('admin')

    def get_available_topics(self):
        return [(topic.name, topic.value) for topic in Topic]

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.topics = SelectMultipleField('Topics',
                                                choices=self.get_available_topics())
        form_class.password2 = PasswordField('New Password')

        return form_class

    def on_model_change(self, form, model, is_created):
        if len(model.password2):
            model.password = utils.hash_password(model.password2)


class RoleAdmin(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')
