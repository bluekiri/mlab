import datetime
import os
import socket

from api_server.entities.domain.worker_mo import Worker
from api_server.repository.mongo.model_repository import get_current_model


def register_worker():
    name = os.getpid()
    model = get_current_model()
    Worker.objects(name=str(name), host_name=socket.gethostname(),
                   host=socket.gethostbyname(socket.gethostname())).update(set__name=str(name),
                                                                           set__host_name=socket.gethostname(),
                                                                           set__host=socket.gethostbyname(
                                                                               socket.gethostname()),
                                                                           set__model=model,
                                                                           set__ts=datetime.datetime.utcnow,
                                                                           upsert=True)
