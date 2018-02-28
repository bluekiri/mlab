# coding: utf-8
import logging

from worker.domain.entities.logs_mo import Logs, LogsTopics
from worker.domain.interactors.get_model import GetModel
from worker.domain.interactors.model_change_listener import ModelChangeListener
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class ModelChangeListenerImp(ModelChangeListener):
    def __init__(self, model_repository: ModelRepository, worker_repository: WorkerRepository,
                 logs_repository: LogsRepository, get_model: GetModel):
        self.get_model = get_model
        self.logs_repository = logs_repository
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)
        self.model_repository = model_repository

    def run(self):
        self.worker_repository.subscribe_on_worker_model_change(
            lambda model_id: self.get_model.switch_and_get_model_by_id(model_id))

