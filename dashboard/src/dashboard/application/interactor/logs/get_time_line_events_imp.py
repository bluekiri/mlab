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

from dashboard.domain.entities.logs import LogsTopics
from dashboard.domain.repositories.logs_repository import LogsRepository
from dashboard.domain.interactor.logs.get_time_line_events import \
    GetTimeLineEvents


class GetTimeLineEventsImp(GetTimeLineEvents):
    def __init__(self, logs_repository: LogsRepository):
        self.logs_repository = logs_repository

    def get_all_time_events(self):
        return self.logs_repository.get_logs_by_topics(
            [LogsTopics.new_model.name])
        # log.ts = log.ts.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
