# coding: utf-8
from domain.entities.model_mo import Model


class ModelRepository:
    def get_current_model(self) -> Model:
        raise NotImplementedError()

    def load_default_model(self):
        raise NotImplementedError()

    def try_load_new_model_instance(self):
        raise NotImplementedError()
