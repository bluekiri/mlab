# coding: utf-8
from benchmark.domain.entities.model_mo import Model


class ModelRepository:

    def get_model_from_id(self, model_id: str):
        raise NotImplementedError()
