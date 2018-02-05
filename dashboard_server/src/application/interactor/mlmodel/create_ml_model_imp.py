# coding:utf-8
from datetime import datetime

from domain.entities.ml_model import MlModel
from domain.interactor.logs.save_model_log_event import SaveModelLogEvent
from domain.interactor.messages.send_message import SendMessage
from domain.interactor.mlmodel.create_ml_model import CreateMlModel
from domain.repositories.model_repository import ModelRepository


class CreateMlModelImp(CreateMlModel):
    def __init__(self, send_message: SendMessage, save_model_log_event: SaveModelLogEvent,
                 model_repository: ModelRepository):
        self.send_message = send_message
        self.save_model_log_event = save_model_log_event
        self.model_repository = model_repository

    def create(self, name: str, score: float, description: str, pickle, creator_id: str,
               images=None):
        model = MlModel(name=name, description=description, ts=datetime.utcnow(),
                        pickle=pickle, score=score)
        self.model_repository.save(model)
        self.save_model_log_event.save_new_model_event(model_id=str(model.pk),
                                                       model_name=model.name, is_system_event=False,
                                                       source_id=creator_id)
        self.send_message.new_model_message(model)
