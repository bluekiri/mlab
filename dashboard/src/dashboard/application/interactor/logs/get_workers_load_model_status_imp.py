from dashboard.domain.interactor.logs.get_workers_load_model_status import GetWorkersLoadModelStatus
from dashboard.domain.repositories.worker_repository import WorkerRepository


class GetWorkersLoadModelStatusImp(GetWorkersLoadModelStatus):
    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository

    def run(self):
        all_workers = self.worker_repository.get_available_workers()
        workers_state = {}
        for worker in all_workers:
            if not worker.up:
                self._append_or_create_items_in_dict(workers_state, "error", worker)
            elif worker.model_loaded and worker.model_error:
                self._append_or_create_items_in_dict(workers_state, "warning", worker)
            else:
                self._append_or_create_items_in_dict(workers_state, "success", worker)
        return workers_state

    @staticmethod
    def _append_or_create_items_in_dict(dictionary, key, item):
        if key in dictionary.keys():
            dictionary[key].append(item)
        else:
            dictionary[key] = [item]
