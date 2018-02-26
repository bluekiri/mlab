# coding: utf-8
import logging

from worker.domain.entities.logs_mo import Logs, LogsTopics
from worker.domain.interactors.model_change_listener import ModelChangeListener
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class ModelChangeListenerImp(ModelChangeListener):
    def __init__(self, model_repository: ModelRepository, worker_repository: WorkerRepository,
                 logs_repository: LogsRepository):
        self.logs_repository = logs_repository
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)
        self.model_repository = model_repository

    def run(self):
        self.worker_repository.subscribe_on_worker_model_change(
            lambda model_id: self._try_to_load_new_model_instance(model_id))

    def _try_to_load_new_model_instance(self, model_id):
        try:
            self.model_repository.try_load_new_model_instance(model_id)
            self.worker_repository.success_model_load()
        except Exception as e:
            log = Logs()
            log.text = str(e)
            log.topic = LogsTopics.worker_error
            log.source_id = self.worker_repository.get_worker_host()
            self.model_repository.try_load_new_model_instance(model_id)
            self.logs_repository.save(log)
            self.worker_repository.set_worker_model_error(log)
