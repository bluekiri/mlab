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

import datetime
from typing import List

from dashboard.domain.entities.logs import Logs, LogsTopics
from dashboard.domain.interactor.logs.save_model_log_event import SaveModelLogEvent
from dashboard.domain.interactor.users.current_user import CurrentUser
from dashboard.domain.repositories.logs_repository import LogsRepository


class SaveModelModelLogEventImp(SaveModelLogEvent):
    def __init__(self, log_repository: LogsRepository, current_user: CurrentUser):
        self.current_user = current_user
        self.log_repository = log_repository

    def _get_empty_log_event(self, topic: LogsTopics, model_name: str, model_id: str,
                             is_system_event: bool, source_id: str = None):
        log = Logs()
        log.ts = datetime.datetime.utcnow()
        log.topic = topic.name
        log.data = {
            "model_name": model_name,
            "model_id": model_id,
        }

        if is_system_event:
            return log

        log.source_id = str(
            self.current_user.get_current_user().pk) if source_id is None else str(source_id)

        return log

    def save_new_model_event(self, model_name: str, model_id: str, is_system_event: bool,
                             source_id: str):
        log = self._get_empty_log_event(LogsTopics.new_model, model_name, model_id, is_system_event,
                                        source_id)
        self.log_repository.save(log)

    def save_activate_model_by_group_event(self, model_name: str, model_id: str, host: List[str],
                                           group_name: str, is_system_event: bool, source_id: str):
        log = self._get_empty_log_event(LogsTopics.activate_model, model_name, model_id, is_system_event,
                                        source_id)
        log.data["host"] = host
        log.data["group"] = group_name
        self.log_repository.save(log)

    def save_activate_model_event(self, model_name: str, model_id: str, host: List[str],
                                  is_system_event: bool, source_id: str):
        log = self._get_empty_log_event(LogsTopics.activate_model, model_name, model_id, is_system_event,
                                        source_id)
        log.data["host"] = host

        self.log_repository.save(log)
