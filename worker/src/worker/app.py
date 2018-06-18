# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Bluekiri V5 BigData Team <bigdata@bluekiri.com>.
#
# This program is free software: you can redistribute it and/or  modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# As a special exception, the copyright holders give permission to link the
# code of portions of this program with the OpenSSL library under certain
# conditions as described in each individual source file and distribute
# linked combinations including the program with the OpenSSL library. You
# must comply with the GNU Affero General Public License in all respects for
# all of the code used other than as permitted herein. If you modify file(s)
# with this exception, you may extend this exception to your version of the
# file(s), but you are not obligated to do so. If you do not wish to do so,
# delete this exception statement from your version. If you delete this
# exception statement from all source files in the program, then also delete
# it in the license file.

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
