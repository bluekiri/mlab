# coding: utf-8
import logging
import os
import socket

from domain.interactors.register_worker import RegisterWorker
from domain.repositories.worker_repository import WorkerRepository


class RegisterWorkerImp(RegisterWorker):
    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)

    def run(self):
        model = get_current_model()
        self.worker_repository.save_worker(str, str(os.getpid()), socket.gethostname(),
                                           socket.gethostbyname(socket.gethostname()), model)
