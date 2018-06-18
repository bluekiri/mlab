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

import logging

from worker.domain.entities.logs_mo import Logs, LogsTopics
from worker.domain.entities.model_mo import Model
from worker.domain.exception.unpickle_model_exception import UnpickleModelException
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class ModelRepositoryImp(ModelRepository):
    singleton_current_model = None

    loading_model = False

    def __init__(self, worker_repository: WorkerRepository,
                 logs_repository: LogsRepository):
        self.logs_repository = logs_repository
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)

    def _build_success_load_model_log(self, model_name, model_id) -> Logs:
        log = Logs()
        log.topic = LogsTopics.activate_model.name
        log.text = "Model loaded successful"
        log.data = {"model_id": str(model_id),
                    "model_name": model_name,
                    "host": self.worker_repository.get_worker_host(),
                    "host_name": self.worker_repository.get_self_worker_model_id()}
        return log

    def _build_error_load_model_log(self, model_name, model_id) -> Logs:
        log = Logs()
        log.topic = LogsTopics.worker_error.name
        log.text = "Error getting current model"
        log.data = {"model_id": str(model_id),
                    "model_name": model_name,
                    "host": self.worker_repository.get_worker_host(),
                    "host_name": self.worker_repository.get_self_worker_model_id()}
        return log

    def get_current_model(self) -> Model:
        if self.singleton_current_model is None:
            self.load_default_model()
        return self.singleton_current_model

    def load_default_model(self):
        model_id = self.worker_repository.get_self_worker_model_id()
        if model_id is None:
            models = Model.objects()
            if len(models) > 0:
                model = list(models)[-1]
                self.logger.info(
                    "Model not found... Loading first mlmodel (%s)" %
                    model.name)
                self.try_load_new_model_instance(model.pk)
            else:
                self.logger.warning("No models found")

                #     try:
                #         model = models[-1]
                #         self.logger.info(
                #             "Model not found... Loading first mlmodel (%s)" %
                #             self.singleton_current_model.name)
                #         model.get_model_instance()
                #         self.singleton_current_model = model
                #
                #     except UnpickleModelException as e:
                #         model = models[-1]
                #         self.logger.error("Error loading (%s)" % model.name)
                #         log = self._build_error_load_model_log(model.name, model.pk)
                #         self.logs_repository.save(log)
                #     except Exception as e:
                #         self.logger.warning("No models found: %s" % e)
                #     finally:
                #         self.loading_model = False
        else:
            self.try_load_new_model_instance(model_id)

    def try_load_new_model_instance(self, model_id: str):
        model = Model.objects(pk=model_id).first()
        if model is None:
            return False
        if (self.singleton_current_model is None or model.pk !=
            self.singleton_current_model.pk) and not self.loading_model:
            self.logger.info("New mlmodel found (%s)" % model.name)
            model_found = Model.objects(pk=model.pk).first()
            self.loading_model = True
            try:
                model_found.get_model_instance()
            except Exception as e:
                self.logger.error("Error unpeckilizing (%s)" % model.name)
                log = self._build_error_load_model_log(model.name, model.pk)
                self.logs_repository.save(log)
                self.worker_repository.set_error_modal_load()
                raise UnpickleModelException(model_id,
                                             self.worker_repository.get_worker_host(),
                                             str(e))
            finally:
                self.loading_model = False

            self.singleton_current_model = model_found
            self.worker_repository.set_success_model_load()

            log = self._build_success_load_model_log(model.name, model.pk)
            self.logs_repository.save(log)

            self.logger.info("New mlmodel loaded (%s)" % model.name)
            return True
        return False

    def get_model_name_by_id(self, model_id: str):
        model_query = Model.objects(pk=model_id)
        try:
            return model_query[0].name
        except Exception:
            return None
