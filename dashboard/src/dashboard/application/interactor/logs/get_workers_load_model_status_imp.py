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

from dashboard.domain.interactor.logs.get_workers_load_model_status import \
    GetWorkersLoadModelStatus
from dashboard.domain.repositories.worker_repository import WorkerRepository


class GetWorkersLoadModelStatusImp(GetWorkersLoadModelStatus):
    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository

    def run(self):
        all_workers = self.worker_repository.get_available_workers()
        workers_state = {}
        for worker in all_workers:
            if not worker.up:
                self._append_or_create_items_in_dict(workers_state, "error",
                                                     worker)
            elif worker.model_loaded and worker.model_error:
                self._append_or_create_items_in_dict(workers_state, "warning",
                                                     worker)
            else:
                self._append_or_create_items_in_dict(workers_state, "success",
                                                     worker)
        return workers_state

    @staticmethod
    def _append_or_create_items_in_dict(dictionary, key, item):
        if key in dictionary.keys():
            dictionary[key].append(item)
        else:
            dictionary[key] = [item]
