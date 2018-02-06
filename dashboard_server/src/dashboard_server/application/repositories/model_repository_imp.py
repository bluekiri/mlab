# coding:utf-8
from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.repositories.model_repository import ModelRepository


class ModelRepositoryImp(ModelRepository):
    def get_model_by_id(self, model_id: str) -> MlModel:
        if model_id is None:
            return None
        return MlModel.objects(pk=model_id).first()

    def save(self, model: MlModel):
        model.save()