# coding:utf-8
from dashboard.domain.entities.message import Message, Topic, SubjectData
from dashboard.domain.entities.ml_model import MlModel
from dashboard.domain.interactor.messages.send_message import SendMessage
from dashboard.domain.repositories.messages_repository import MessageRepository


class SendMessageImp(SendMessage):
    def __init__(self, messages_repository: MessageRepository):
        self.messages_repository = messages_repository

    def new_model_message(self, model: MlModel):
        message = Message()
        message.topic = Topic.new_model.name
        message.subject_data = SubjectData.new_model.name
        message.subject = SubjectData.new_model.value['text']
        message.text = "Model name %s" % model.name
        self.messages_repository.save_message(message)
