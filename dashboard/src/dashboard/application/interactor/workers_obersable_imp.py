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

from typing import List

from dashboard.domain.interactor.workers_listener_event import \
    WorkersListenerEvent
from dashboard.domain.repositories.worker_repository import WorkerRepository


class WorkersListenerEventImp(WorkersListenerEvent):
    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository
        self.worker_repository.subscribe_worker_down_callback(
            self._on_worker_change)
        self.current_workers_status = self.worker_repository.get_available_workers()

    def _on_worker_change(self, workers_id: List[str]):
        if len(workers_id) - len(self.current_workers_status) > 0:
            print("new")
        elif len(self.current_workers_status) - len(workers_id):
            print("delete")
        else:
            print("updated")

    def on_worker_up(self):
        pass

    def on_new_worker(self):
        pass

    def on_worker_down(self):
        pass
