#!/usr/bin/env python3
import inspect
import logging
import os
import signal
import sys
from logging.config import fileConfig

import connexion

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from api_server.interactor.worker.active_listener import active_listener
from api_server.interactor.worker.worker_interactor import register_worker
from api_server.interactor.register_sigint_interactor import signal_handler
from api_server.encoder import JSONEncoder

conf_dir = os.path.join(currentdir, "conf")
logging.config.fileConfig(os.path.join(conf_dir, 'logging.ini'))


# from .encoder import JSONEncoder

def initialize_worker():
    logging.info("Worker with pid %s" % str(os.getpid()))
    register_worker()
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGSEGV, signal_handler)


logging.info("Init worker")
initialize_worker()
active_listener()

app_wrapper = connexion.App(__name__, 9090, specification_dir='./swagger/')
app_wrapper.app.json_encoder = JSONEncoder
app_wrapper.add_api('swagger.yaml', arguments={'title': 'Book prob documentation'})

# app_wrapper.app.conf.from_pyfile(os.path.join(conf_dir, 'conf.py'))

if __name__ == '__main__':
    logging.info("Init app")
    app_wrapper.run()

    # gunicorn --access-logfile ~/api_worker.log -w 4 -t 90 -b 0.0.0.0:9090 app:app_wrapper
