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

import gridfs
from flask import request, Response
from flask_admin import expose
from flask_admin.contrib.mongoengine import ModelView
from flask_admin.form import rules
from flask_security.core import current_user
from mongoengine.connection import get_db
from werkzeug.exceptions import abort

from dashboard.application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from dashboard.domain.interactor.logs.save_model_log_event import \
    SaveModelLogEvent
from dashboard.domain.interactor.users.current_user import CurrentUser
from dashboard.domain.repositories.model_repository import ModelRepository


class MlModelView(ModelView, metaclass=ViewSecurityListeners):
    can_edit = False
    can_view_details = True
    can_view = True
    can_create = False
    can_delete = False
    column_default_sort = ('ts', True)
    can_download = False

    # details_template = 'mlmodel/details.html'

    def __init__(self, model, model_repository: ModelRepository,
                 save_model_log_event: SaveModelLogEvent,
                 current_user: CurrentUser,
                 name, menu_icon_type,
                 menu_icon_value):
        super().__init__(model, name=name, menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self.model_repository = model_repository
        self.current_user = current_user
        self.save_model_log_event = save_model_log_event

    def is_accessible(self):
        return current_user.is_authenticated

    def has_edit_role(self):
        self.can_edit = True

    def has_admin_role(self):
        self.can_edit = True
        self.can_delete = True
        self.can_create = True

    def on_model_change(self, form, model, is_created):
        model.set_pk()
        self.save_model_log_event.save_new_model_event(model.name,
                                                       str(model.pk), False,
                                                       self.current_user.get_current_user().pk)


    @expose('/api/file/')
    def api_file_view(self):
        pk = request.args.get('id')
        coll = request.args.get('coll')
        db = request.args.get('db', 'default')

        if not pk or not coll or not db:
            abort(404)

        fs = gridfs.GridFS(get_db(db), coll)

        data = fs.get(self.object_id_converter(pk))
        if not data:
            abort(404)

        return Response(data.read(),
                        content_type='application/octet-stream',
                        headers={'Content-Length': data.length,
                                 'Content-Disposition': 'attachment',
                                 'filename': "downloaded.pdf"})
