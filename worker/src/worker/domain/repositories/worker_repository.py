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


class WorkerRepository:
    def get_worker_host(self):
        raise NotImplementedError()

    def initialize_event_listener(self):
        raise NotImplementedError()

    def remove_worker_from_host(self, worker_name: str, host_name: str):
        raise NotImplementedError()

    def subscribe_on_worker_model_change(self, callback_function):
        raise NotImplementedError()

    def save_worker(self, number_of_instances: int):
        raise NotImplementedError()

    def get_self_worker_model_id(self) -> str:
        raise NotImplementedError()

    def set_success_model_load(self):
        raise NotImplementedError()

    def set_error_modal_load(self):
        raise NotImplementedError()

    def is_current_worker_loaded_on_zoo(self):
        raise NotImplementedError
