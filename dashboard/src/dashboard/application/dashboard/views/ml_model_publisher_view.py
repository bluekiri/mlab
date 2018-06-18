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

import json
import html

import pytz
import tzlocal
import html
from flask import request
from flask import url_for
from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required
from flask_security.decorators import roles_required

from dashboard.application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from dashboard.domain.entities.ml_model import MlModel
from dashboard.domain.interactor.logs.get_workers_load_model_status import \
    GetWorkersLoadModelStatus
from dashboard.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor
from dashboard.domain.interactor.users.current_user import CurrentUser
from dashboard.domain.interactor.users.users_privileges import UsersPrivileges


class MLModelPublisherView(BaseView, metaclass=ViewSecurityListeners):
    can_edit = True

    def __init__(self, users_privilages: UsersPrivileges,
                 orchestation_interactor: OrchestationInteractor,
                 get_workers_load_model_status: GetWorkersLoadModelStatus,
                 current_user: CurrentUser, name,
                 menu_icon_type, menu_icon_value):
        super().__init__(name=name, menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self.get_workers_load_model_status = get_workers_load_model_status
        self.current_user = current_user
        self.users_privilages = users_privilages
        self.orchestation_interactor = orchestation_interactor

    @login_required
    @expose()
    def index(self):
        group_of_workers, workers_without_group = self.orchestation_interactor.get_group_workers()

        worker_status = self.get_workers_load_model_status.run()
        worker_status_flatten = {
            status: [worker.host_name for worker in workers]
            for status, workers in worker_status.items()}

        def get_worker_status_from_hostname(hostname: str):
            for key, value in worker_status_flatten.items():
                if hostname in value:
                    return key
            return 'success'

        for group, workers in group_of_workers.items():
            for worker in workers:
                worker["status"] = get_worker_status_from_hostname(
                    worker["hostname"])
        for worker_without_group in workers_without_group:
            worker_without_group["status"] = get_worker_status_from_hostname(
                worker_without_group["hostname"])
        return self.render('ml_model_publisher/ml_model_publisher.html',
                           group_of_workers=group_of_workers,
                           workers_without_group=workers_without_group,
                           has_active_model_permissions=self.current_user.has_admin_role(),
                           )

    @expose('/models', methods=('GET',))
    def models(self):
        return json.dumps(
            [(str(model.pk), html.escape(self._format_model_name(model))) for
             model in
             MlModel.objects().order_by('-ts')])

    def _format_model_name(self, model):
        local_time_zone = tzlocal.get_localzone()
        local_time = model.ts.replace(tzinfo=pytz.utc).astimezone(
            local_time_zone)
        return model.name + " - " + local_time.strftime('%Y-%m-%d %H:%M:%S')

    def _get_file_url(self, path):
        """
            Return static file url
            :param path:
                Static file path
        """
        if self.is_file_editable(path):
            route = '.edit'
        else:
            route = '.download'

        return self.get_url(route, path=path)

    @login_required
    @roles_required('admin', )
    @expose('/enable_auto_publisher', methods=('POST',))
    def enable_auto_publisher(self):
        host_name = request.form.get("host_name")
        enable = request.form.get("enable")

        self.orchestation_interactor.set_auto_model_publisher(host_name, enable)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}

    @login_required
    @roles_required('admin', )
    @expose('/change_model', methods=('POST',))
    def change_model(self):
        host_name = request.form.get("host_name")
        model_id = request.form.get("model_id")

        self.orchestation_interactor.load_model_on_host(host_name, model_id)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}

    @login_required
    @roles_required('admin', )
    @expose('/change_group_model', methods=('POST',))
    def change_group_model(self):
        group_name = request.form.get("group_name")
        model_id = request.form.get("model_id")

        self.orchestation_interactor.load_model_on_group(group_name, model_id)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}

    @login_required
    @expose('/groups', methods=('GET',))
    def get_groups(self):
        return json.dumps(
            map(html.escape, self.orchestation_interactor.get_groups()))

    @login_required
    @roles_required('admin', )
    @expose('/set_group', methods=('POST',))
    def set_group(self):
        host_name = request.form.get("host_name")
        group = request.form.get("group")

        self.orchestation_interactor.set_group_to_worker(host_name, group)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}

    @login_required
    @roles_required('admin', )
    @expose('/worker', methods=('DELETE',))
    def delete(self):
        host_name = request.form.get("host_name")
        self.orchestation_interactor.remove_disconnected_worker(host_name)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}
