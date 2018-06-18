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
