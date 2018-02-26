import datetime
from enum import Enum
import logging
from mongoengine import connect, Document, DateTimeField, StringField, DictField

from worker.application.conf.config import MONGO_CONNECTION_URI, MONGO_DATABASE

connect(host=MONGO_CONNECTION_URI, db=MONGO_DATABASE, connect=False)
logger = logging.getLogger()


class LogsTopics(Enum):
    new_model = "New Model"
    activate_model = "Activate Model"
    worker_error = "Worker Error"


class Logs(Document):
    ts = DateTimeField(default=datetime.datetime.utcnow)
    topic = StringField()
    data = DictField()
    text = StringField()
    source_id = StringField()
