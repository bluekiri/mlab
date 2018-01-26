# coding: utf-8
from typing import List

from domain.interactor.workers_listener_event import WorkersListenerEvent
from domain.repositories.worker_repository import WorkerRepository


class WorkersListenerEventImp(WorkersListenerEvent):
    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository
        self.worker_repository.subscribe_worker_down_callback(self._on_worker_change)
        self.current_workers_status = self.worker_repository.get_available_workers()

    def _on_worker_change(self, workers_id: List[str]):
        if len(workers_id) - len(self.current_workers_status) > 0:
            print("new")
        elif len(self.current_workers_status) - len(workers_id):
            print("delete")
        else:
            print("updated")

    def on_worker_up(self):
        pass

    def on_new_worker(self):
        pass

    def on_worker_down(self):
        pass
