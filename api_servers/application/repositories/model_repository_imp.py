# coding: utf-8
import logging
import os
import socket

from domain.entities.model_mo import Model
from domain.entities.worker_mo import Worker
from domain.repositories.model_repository import ModelRepository


class ModelRepositoryImp(ModelRepository):
    singleton_current_model = None
    loading_model = False

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_current_model(self) -> Model:
        if self.singleton_current_model is None:
            self.load_default_model()
        return self.singleton_current_model

    def load_default_model(self):
        model = self._get_model_for_this_host()
        if model is None:
            self.loading_model = True
            try:
                singleton_current_model = Model.objects().first()
                singleton_current_model.get_model_instance()
                self.logger.info(
                    "Model not found... Loading first model (%s)" % singleton_current_model.name)
            except Exception as e:
                self.logger.warning("No models found: %s" % e)
            finally:
                self.loading_model = False
        else:
            self.try_load_new_model_instance()

    def try_load_new_model_instance(self):
        model = self._get_model_for_this_host()
        if model is None:
            return False
        if model.pk != self.singleton_current_model.pk and not self.loading_model:
            self.logger.info("New model found (%s)" % model.name)
            model_found = Model.objects(pk=model.pk).first()
            self.loading_model = True
            try:
                model_found.get_model_instance()
                self.singleton_current_model = model_found
            finally:
                self.loading_model = False
            self.logger.info("New model loaded (%s)" % model.name)
            return True
        return False

    def _get_model_for_this_host(self):
        pid_name = os.getpid()
        worker = Worker.objects(name=str(pid_name), host_name=socket.gethostname(),
                                host=socket.gethostbyname(socket.gethostname())).first()
        if worker is not None and worker.model is not None:
            return worker.model
