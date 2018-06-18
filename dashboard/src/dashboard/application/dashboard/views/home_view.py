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

import html

from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required

from dashboard.domain.interactor.logs.get_time_line_events import \
    GetTimeLineEvents
from dashboard.domain.interactor.logs.get_workers_load_model_status import \
    GetWorkersLoadModelStatus


class HomeView(BaseView):
    def __init__(self, get_line_time_events: GetTimeLineEvents,
                 get_workers_load_model_status: GetWorkersLoadModelStatus,
                 name=None, category=None,
                 endpoint=None, url=None, template='index.html',
                 menu_class_name=None, menu_icon_type=None,
                 menu_icon_value=None):
        super().__init__(name or "Home",
                         category,
                         endpoint or 'admin',
                         '/admin' if url is None else url,
                         'static',
                         menu_class_name=menu_class_name,
                         menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self.get_workers_load_model_status = get_workers_load_model_status
        self.get_line_time_events = get_line_time_events
        self._template = template

    @login_required
    @expose()
    def index(self):
        logs = self.get_line_time_events.get_all_time_events()
        for log in logs:
            log.data['model_name'] = html.escape(log.data['model_name'])
        worker_status = self.get_workers_load_model_status.run()
        return self.render(self._template, logs=logs,
                           worker_status=worker_status)
