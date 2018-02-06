# coding: utf-8
from api_server.application.repositories.model_repository import ModelRepository


class BaseModelController:
    def __init__(self, model_repository: ModelRepository):
        self.model_repository = model_repository
        self.model_repository.get_current_model()
