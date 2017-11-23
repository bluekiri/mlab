# coding: utf-8
from dashboard_server.domain.entities.ml_model import MlModel


class SendMessage:
    def new_model_message(self, model: MlModel):
        raise NotImplementedError()
