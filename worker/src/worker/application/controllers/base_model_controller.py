# coding: utf-8
from worker.domain.interactors.get_current_model import GetCurrentModel


class BaseModelController:
    def __init__(self, get_current_model: GetCurrentModel):
        self.model_repository = get_current_model
        self.model_repository.get_current_model()
