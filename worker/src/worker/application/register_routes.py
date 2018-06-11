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
