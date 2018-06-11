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


class SaveModelLogEvent:
    def save_new_model_event(self, model_name: str, model_id: str,
                             is_system_event: bool, source_id: str):
        raise NotImplementedError()

    def save_activate_model_event(self, model_name: str, model_id: str,
                                  host: List[str],
                                  is_system_event: bool, source_id: str):
        raise NotImplementedError()

    def save_activate_model_by_group_event(self, model_name: str, model_id: str,
                                           host: List[str],
                                           group_name: str,
                                           is_system_event: bool,
                                           source_id: str):
        raise NotImplementedError()
