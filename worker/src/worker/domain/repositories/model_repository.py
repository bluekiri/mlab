# coding: utf-8
from worker.domain.entities.model_mo import Model


class ModelRepository:
    def get_current_model(self) -> Model:
        raise NotImplementedError()

    def load_default_model(self):
        raise NotImplementedError()

    def try_load_new_model_instance(self, model_id: str):
        raise NotImplementedError()

    def get_model_name_by_id(self, model_id: str):
        raise NotImplementedError()
