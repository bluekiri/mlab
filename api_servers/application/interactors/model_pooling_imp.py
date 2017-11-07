# coding: utf-8
import logging
import threading

from domain.interactors.model_pooling import ModelPooling
from domain.repositories.model_repository import ModelRepository


class ModelPoolingImp(ModelPooling):
    def __init__(self, model_repository: ModelRepository):
        self.logger = logging.getLogger(__name__)
        self.model_repository = model_repository

    def run(self):
        threading.Timer(5.0, self.run).start()
        self.model_repository.try_load_new_model_instance()
