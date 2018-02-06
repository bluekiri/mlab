# coding: utf-8
import logging

from api_servers.domain.entities.model_mo import Model
from api_servers.domain.repositories.model_repository import ModelRepository
from api_servers.domain.repositories.worker_repository import WorkerRepository


class ModelRepositoryImp(ModelRepository):
    singleton_current_model = None
    loading_model = False

    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository
        self.logger = logging.getLogger(__name__)

    def get_current_model(self) -> Model:
        if self.singleton_current_model is None:
            self.load_default_model()
        return self.singleton_current_model

    def load_default_model(self):
        model_id = self.worker_repository.get_self_worker_model_id()
        if model_id is None:
            self.loading_model = True
            try:
                self.singleton_current_model = Model.objects().first()
                self.singleton_current_model.get_model_instance()
                self.logger.info(
                    "Model not found... Loading first mlmodel (%s)" % self.singleton_current_model.name)
            except Exception as e:
                self.logger.warning("No models found: %s" % e)
            finally:
                self.loading_model = False
        else:
            self.try_load_new_model_instance(model_id)

    def try_load_new_model_instance(self, model_id: str):
        # model = self._get_model_for_this_host()
        model = Model.objects(pk=model_id).first()
        if model is None:
            return False
        if (
                        self.singleton_current_model is None or model.pk != self.singleton_current_model.pk) and not self.loading_model:
            self.logger.info("New mlmodel found (%s)" % model.name)
            model_found = Model.objects(pk=model.pk).first()
            self.loading_model = True
            try:
                model_found.get_model_instance()
                self.singleton_current_model = model_found
            finally:
                self.loading_model = False
            self.logger.info("New mlmodel loaded (%s)" % model.name)
            return True
        return False