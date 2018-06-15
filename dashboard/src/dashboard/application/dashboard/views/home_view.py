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
