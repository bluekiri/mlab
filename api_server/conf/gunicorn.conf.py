import inspect
import os
import socket

import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, os.path.dirname(parentdir))

from api_server.entities.domain.worker_mo import Worker

name = "hbp_api_server"
bind = "0.0.0.0:9090"
workers = 3
timeout = 90
graceful_timeout = 60

log_file = "/var/log/hbp_api_server/hbp_api_server_gunicorn.log"
keepalive = 2


def _remove_worker_pid(pid):
    workers = Worker.objects(name=pid, host_name=socket.gethostname())
    for worker in workers:
        worker.delete()


def worker_abort(worker):
    _remove_worker_pid(str(worker.ppid))


def worker_exit(server, worker):
    _remove_worker_pid(str(worker.ppid))


def child_exit(server, worker):
    _remove_worker_pid(str(worker.ppid))
