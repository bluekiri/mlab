import socket

from application.conf.config import MONGO_CONNECTION_URI

print(MONGO_CONNECTION_URI)
from api_servers.domain.entities.worker_mo import Worker

timeout = 90
graceful_timeout = 60
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
