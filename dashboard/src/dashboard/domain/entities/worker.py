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


class Worker(object):
    def __init__(self, host_name, host, model, number_of_instances, group, up, ts, model_error: bool,
                 model_loaded: bool,auto_model_publisher:bool):
        self.auto_model_publisher = auto_model_publisher
        self.number_of_instances = number_of_instances
        self.model = model
        self.host = host
        self.host_name = host_name
        self.group = group
        self.up = up
        self.ts = ts
        self.model_error = model_error
        self.model_loaded = model_loaded
