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

from flask import make_response
from flask import request

from dashboard.domain.interactor.mlmodel.create_ml_model import CreateMlModel
from dashboard.domain.interactor.users.token_verification import \
    TokenVerification
from dashboard.domain.repositories.worker_repository import WorkerRepository


def register_model_methods(api, token_verification: TokenVerification,
                           create_ml_model: CreateMlModel,
                           worker_repository: WorkerRepository):
    @api.route('/mlmodel', methods=('POST',))
    def model():
        if not _is_valid_request_model():
            return make_response('Bad request', 400)
        token = request.args['token']

        if not token_verification.is_valid_token(token):
            return "Invalid token", 403

        pickle = request.files['file']

        data = request.form

        description = data['description'] if 'description' in data else ''

        model_id = create_ml_model.create(description=description,
                                          pickle=pickle,
                                          score=data['score'],
                                          creator_id=token, name=data['name'])
        _active_model_in_all_workers(str(model_id))
        return make_response('Ok', 200)

    def _active_model_in_all_workers(model_id):
        all_workers = worker_repository.get_available_workers()

        for worker in all_workers:
            if worker_repository.is_enable_auto_model_publication(
                    worker.host_name):
                worker_repository.set_model_in_worker(worker.host_name,
                                                      model_id)

    def _is_valid_request_model():
        return 'token' in request.args and 'file' in request.files and 'name' in request.form and 'score' in request.form
