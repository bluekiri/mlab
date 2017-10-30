# coding: utf-8
from domain.entities.model_mo import Model


class WorkerRepository:
    def remove_worker_from_host(self, worker_name: str, host_name: str):
        raise NotImplementedError()

    def save_worker(self, name: str, host_name: str, host: str, model: Model):
        raise NotImplementedError()
