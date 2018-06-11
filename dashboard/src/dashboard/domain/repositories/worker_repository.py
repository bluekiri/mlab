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

from dashboard.domain.entities.worker import Worker


class WorkerRepository:
    def get_available_workers(self) -> List[Worker]:
        raise NotImplementedError()

    def get_workers_host_by_group(self, group: str) -> List[str]:
        raise NotImplementedError()

    def set_model_in_worker(self, worker_host: str, model_id: str):
        raise NotImplementedError()

    def set_group_in_worker(self, worker_host: str, group: str):
        raise NotImplementedError()

    def get_groups(self):
        raise NotImplementedError()

    def subscribe_worker_down_callback(self, callback):
        raise NotImplementedError()

    # def get_all_workers(self):
    #     raise NotImplementedError()

    def is_enable_auto_model_publication(self, worker_host):
        raise NotImplementedError()

    def set_auto_model_publisher(self, worker_host: str, enable: bool):
        raise NotImplementedError()
