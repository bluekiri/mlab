# coding: utf-8
import logging
import os
import socket

from domain.interactors.register_worker import RegisterWorker
from domain.repositories.model_repository import ModelRepository
from domain.repositories.worker_repository import WorkerRepository


class RegisterWorkerImp(RegisterWorker):
    def __init__(self, worker_repository: WorkerRepository, model_repository: ModelRepository):
        self.model_repository = model_repository
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)

    def run(self):
        model = self.model_repository.get_current_model()
        # self.worker_repository.save_worker(str(os.getpid()), socket.gethostname(),
        #                                    socket.gethostbyname(socket.gethostname()), model)
        # self.logger.info("Worker Registered")
