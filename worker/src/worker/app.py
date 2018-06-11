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


import logging.config
import os
from wsgiref import simple_server

import falcon
import yaml

from worker.application.conf.config import SERVICE_PORT
from worker.application.datasource.zk_datasource_imp import ZKDatasourceImp
from worker.application.interactors.send_mail_imp import SendMailImp
from worker.application.interactors.get_model_imp import GetModelImp
from worker.application.interactors.model_change_listener_imp import \
    ModelChangeListenerImp
from worker.application.register_routes import register_routes
from worker.application.repositories.logs_repository_imp import LogsRepositoryImp
from worker.application.repositories.model_repository_imp import ModelRepositoryImp
from worker.application.repositories.user_repository_imp import UserRepositoryImp
from worker.application.repositories.worker_repository_imp import WorkerRepositoryImp
from worker.application.util import CURRENT_APPLICATION_PATH, ASSETS_APPLICATION_PATH


def setup_logging(default_path=CURRENT_APPLICATION_PATH, default_level=logging.INFO,
                  env_key='API-SERVER'):
    # path = default_path + '/conf/logging.yaml'
    path = "NONE"
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    return logging.getLogger(__name__)


logger = setup_logging()
zk_datasource = ZKDatasourceImp()

logs_repository = LogsRepositoryImp()
worker_repository = WorkerRepositoryImp(zk_datasource)
model_repository = ModelRepositoryImp(worker_repository, logs_repository)
user_repository = UserRepositoryImp()

send_mail = SendMailImp(user_repository)
get_model = GetModelImp(logs_repository, worker_repository, model_repository, send_mail)
model_change_listener = ModelChangeListenerImp(model_repository, worker_repository,
                                               logs_repository, get_model)

logger.info(open(ASSETS_APPLICATION_PATH + '/title.txt', 'r').read())
logger.info("Starting loading server configuration...")

app = falcon.API()

worker_repository.initialize_event_listener()
model_change_listener.run()

register_routes(app, get_model)

logger.info("Server loaded")


def run():
    httpd = simple_server.make_server('0.0.0.0', int(SERVICE_PORT), app)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
