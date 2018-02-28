# coding: utf-8
from worker.domain.interactors.get_model import GetModel


class BaseModelController:
    def __init__(self, get_current_model: GetModel):
        self.model_repository = get_current_model
        self.model_repository.get_current_model()
