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
                                 'filename': "model.p"})
