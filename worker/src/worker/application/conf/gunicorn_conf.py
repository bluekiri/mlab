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

import time

from worker.application.datasource.zk_datasource_imp import ZKDatasourceImp
from worker.application.repositories.worker_repository_imp import \
    WorkerRepositoryImp

timeout = 90
graceful_timeout = 60
keepalive = 2

zk_datasource = ZKDatasourceImp()
worker_repository = WorkerRepositoryImp(zk_datasource)


def on_starting(server):
    max_tries = 15
    tries = 0
    while worker_repository.is_current_worker_loaded_on_zoo() and tries < max_tries:
        time.sleep(1)
        tries += 1
        if tries == max_tries:
            raise TimeoutError()

    worker_repository.save_worker(server.cfg.workers)
