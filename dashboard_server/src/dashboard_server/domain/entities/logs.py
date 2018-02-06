# coding: utf-8
import datetime
from enum import Enum

from dashboard_server.application.repositories.mongo_repository import get_mongo_connection

db = get_mongo_connection()


class LogsTopics(Enum):
    new_model = "New Model"
    activate_model = "Activate Model"


class Logs(db.Document):
    ts = db.DateTimeField(default=datetime.datetime.utcnow)
    topic = db.StringField()
    data = db.DictField()
    text = db.StringField()
    source_id = db.StringField()
