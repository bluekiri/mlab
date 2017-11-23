# coding:utf-8
from datetime import datetime

from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.interactor.mlmodel.create_ml_model import CreateMlModel
from dashboard_server.domain.repositories.model_repository import ModelRepository


class CreateMlModelImp(CreateMlModel):
    def __init__(self, model_repository: ModelRepository):
        self.model_repository = model_repository

    def create(self, name: str, score: float, description: str, pickle, images):
        model = MlModel(name=name, description=description, ts=datetime.utcnow(),
                        pickle=pickle).save()
        self.model_repository.save(model)
