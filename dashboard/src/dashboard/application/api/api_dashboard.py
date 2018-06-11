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

from flask import Blueprint

from dashboard.application.api.model_api import register_model_methods
from dashboard.domain.interactor.mlmodel.create_ml_model import CreateMlModel
from dashboard.domain.interactor.users.token_verification import \
    TokenVerification
from dashboard.domain.repositories.worker_repository import WorkerRepository


class ApiDashboard:
    def __init__(self, token_verification: TokenVerification,
                 create_ml_model: CreateMlModel,
                 worker_repository: WorkerRepository):
        self.worker_repository = worker_repository
        self.create_ml_model = create_ml_model

        self.token_verification = token_verification

        self.api = Blueprint('api', __name__, url_prefix='/api')

        self.register_api_endpoints()

    def get_blueprint(self):
        return self.api

    def register_api_endpoints(self):
        register_model_methods(self.api, self.token_verification,
                               self.create_ml_model, self.worker_repository)
