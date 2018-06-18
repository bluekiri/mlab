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
