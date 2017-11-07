# coding: utf-8
import logging
from datetime import datetime

from domain.entities.model_mo import Model
from domain.entities.worker_mo import Worker
from domain.repositories.worker_repository import WorkerRepository


class WorkerRepositoryImp(WorkerRepository):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def remove_worker_from_host(self, worker_name: str, host_name: str):
        for worker in Worker.objects(name=str(worker_name), host_name=str(host_name)):
            self.logger.info("Removing %s from database..." % str(worker_name))
            worker.delete()

    def save_worker(self, name: str, host_name: str, host: str, model: Model):
        if model is not None:
            Worker.objects(name=name, host_name=host_name, host=host).update(set__name=name,
                                                                             set__host_name=host_name,
                                                                             set__host=host,
                                                                             set__model=model.pk,
                                                                             set__ts=datetime.utcnow(),
                                                                             upsert=True)
        else:
            Worker.objects(name=name, host_name=host_name, host=host).update(set__name=name,
                                                                             set__host_name=host_name,
                                                                             set__host=host,
                                                                             set__ts=datetime.utcnow(),
                                                                             upsert=True)
