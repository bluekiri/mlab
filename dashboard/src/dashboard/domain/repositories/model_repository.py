# coding: utf-8
from dashboard.domain.entities.ml_model import MlModel


class ModelRepository:
    def save(self, model: MlModel):
        raise NotImplementedError()

    def get_model_by_id(self, model_id: str) -> MlModel:
        raise NotImplementedError()
