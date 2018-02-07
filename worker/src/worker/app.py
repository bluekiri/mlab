# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging.config
import os
from wsgiref import simple_server

import falcon
import yaml

from worker.application.conf.config import SERVICE_PORT
from worker.application.datasource.zk_datasource_imp import ZKDatasourceImp
from worker.application.interactors.model_change_listener_imp import ModelChangeListenerImp
from worker.application.register_routes import register_routes
from worker.application.repositories.model_repository_imp import ModelRepositoryImp
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
worker_repository = WorkerRepositoryImp(zk_datasource)
model_repository = ModelRepositoryImp(worker_repository)

model_change_listener = ModelChangeListenerImp(model_repository, worker_repository)

logger.info(open(ASSETS_APPLICATION_PATH + '/title.txt', 'r').read())
logger.info("Starting loading server configuration...")

app = falcon.API()

worker_repository.initialize_event_listener()
model_change_listener.run()

register_routes(app, model_repository)

logger.info("Server loaded")

if __name__ == "__main__":
    httpd = simple_server.make_server('0.0.0.0', SERVICE_PORT, app)
    httpd.serve_forever()
