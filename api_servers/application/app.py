# -*- coding: utf-8 -*-

import falcon
import os
import logging.config

import yaml

from api_servers.application.register_routes import register_routes
from api_servers.application.util import CURRENT_APPLICATION_PATH, ASSETS_APPLICATION_PATH


def setup_logging(
        default_path=CURRENT_APPLICATION_PATH,
        default_level=logging.INFO,
        env_key='API-SERVER'):
    """Setup logging configuration

    """
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

logger.info(open(ASSETS_APPLICATION_PATH + '/title.txt', 'r').read())
logger.info("Starting loading server configuration...")
api = falcon.API()
register_routes(api)
logger.info("Server loaded")
