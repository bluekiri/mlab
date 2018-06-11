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

import logging

from worker.domain.interactors.get_model import GetModel
from worker.domain.interactors.model_change_listener import ModelChangeListener
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class ModelChangeListenerImp(ModelChangeListener):
    def __init__(self, model_repository: ModelRepository,
                 worker_repository: WorkerRepository,
                 logs_repository: LogsRepository, get_model: GetModel):
        self.get_model = get_model
        self.logs_repository = logs_repository
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)
        self.model_repository = model_repository

    def run(self):
        self.worker_repository.subscribe_on_worker_model_change(
            lambda model_id: self.get_model.switch_and_get_model_by_id(
                model_id))
