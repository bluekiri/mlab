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


from worker.domain.entities.logs_mo import LogsTopics
from worker.domain.exception.unpickle_model_exception import \
    UnpickleModelException
from worker.domain.interactors.send_mail import SendMail
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.interactors.get_model import GetModel
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class GetModelImp(GetModel):
    def __init__(self, logs_repository: LogsRepository,
                 worker_repository: WorkerRepository,
                 model_repository: ModelRepository, send_mail: SendMail):
        self.send_mail = send_mail
        self.model_repository = model_repository
        self.worker_repository = worker_repository
        self.logs_repository = logs_repository

    def get_current_model(self):
        global model
        model = None
        try:
            model = self.model_repository.get_current_model()
            return model
        except UnpickleModelException as e:
            self.worker_repository.set_error_modal_load()
            self._send_model_error_alert(e)

    def _send_model_error_alert(self, exception: Exception):
        self.send_mail.send_to_topic(LogsTopics.worker_error.name,
                                     str(exception),
                                     "Worker error")

    def switch_and_get_model_by_id(self, model_id):
        try:
            self.model_repository.try_load_new_model_instance(model_id)
            return self.model_repository.get_current_model()
        except UnpickleModelException as e:
            self._send_model_error_alert(e)
            self.worker_repository.set_error_modal_load()
