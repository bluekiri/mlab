# coding: utf-8
from dashboard_server.domain.entities.ml_model import MlModel


class ModelRepository:
    def save(self, model: MlModel):
        raise NotImplementedError()
