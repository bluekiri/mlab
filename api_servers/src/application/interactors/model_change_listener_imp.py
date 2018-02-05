# coding: utf-8
import logging

from domain.interactors.model_change_listener import ModelChangeListener
from domain.repositories.model_repository import ModelRepository
from domain.repositories.worker_repository import WorkerRepository


class ModelChangeListenerImp(ModelChangeListener):
    def __init__(self, model_repository: ModelRepository, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)
        self.model_repository = model_repository

    def run(self):
        # self.model_repository.try_load_new_model_instance()
        self.worker_repository.subscribe_on_worker_model_change(
            lambda model_id: self.model_repository.try_load_new_model_instance(model_id))
