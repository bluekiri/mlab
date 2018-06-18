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

from falcon import API

from worker.application.controllers.monitor_controller import MonitorController
from worker.application.controllers.dummy_model_controller import \
    DummyModelController
from worker.application.controllers.swagger_controller import SwaggerController
from worker.domain.interactors.get_model import GetModel
from worker.application.util import STATIC_APPLICATION_PATH


def register_routes(falcon_api: API, get_current_model: GetModel):
    falcon_api.add_route('/', SwaggerController())
    falcon_api.add_route('/api/hc', MonitorController())
    falcon_api.add_route('/api/mlmodel', DummyModelController(
        get_current_model=get_current_model))
    falcon_api.add_static_route('/static', STATIC_APPLICATION_PATH)
