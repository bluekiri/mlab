# coding: utf-8
from typing import List

from dashboard.domain.entities.worker import Worker


class WorkerRepository:
    def get_available_workers(self) -> List[Worker]:
        raise NotImplementedError()

    def get_workers_host_by_group(self, group: str) -> List[str]:
        raise NotImplementedError()

    def set_model_in_worker(self, worker_host: str, model_id: str):
        raise NotImplementedError()

    def set_group_in_worker(self, worker_host: str, group: str):
        raise NotImplementedError()

    def get_groups(self):
        raise NotImplementedError()

    def subscribe_worker_down_callback(self, callback):
        raise NotImplementedError()

    def get_all_workers(self):
        raise NotImplementedError()
