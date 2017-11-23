# coding:utf-8
from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.repositories.model_repository import ModelRepository


class ModelRepositoryImp(ModelRepository):
    def save(self, model: MlModel):
        model.save()
