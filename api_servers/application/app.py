# -*- coding: utf-8 -*-

import logging.config
import os
import signal
import socket
from wsgiref import simple_server

import falcon
import yaml

from api_servers.application.register_routes import register_routes
from api_servers.application.util import CURRENT_APPLICATION_PATH, ASSETS_APPLICATION_PATH
from application.repositories.worker_repository_imp import WorkerRepositoryImp


def setup_logging(default_path=CURRENT_APPLICATION_PATH, default_level=logging.INFO,
                  env_key='API-SERVER'):
    path = default_path + '/conf/loggin.yaml'
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
worker_repository = WorkerRepositoryImp()


def signal_handler(signal, frame):
    worker_repository.remove_worker_from_host(os.getpid(), socket.gethostname())


def initialize_worker():
    logger.info("Loading signals handlers...")
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGSEGV, signal_handler)


logger.info(open(ASSETS_APPLICATION_PATH + '/title.txt', 'r').read())
logger.info("Starting loading server configuration...")

api = falcon.API()

register_routes(api)

initialize_worker()

logger.info("Server loaded")

if __name__ == "__main__":
    httpd = simple_server.make_server('0.0.0.0', 9090, api)
    httpd.serve_forever()
