import os
import socket

from api_server.entities.domain.worker_mo import Worker


def signal_handler(signal, frame):
    # TODO drop worker from data base repository
    workers = Worker.objects(name=str(os.getpid()), host_name=socket.gethostname())
    for worker in workers:
        worker.delete()
