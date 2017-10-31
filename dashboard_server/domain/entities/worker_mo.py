import datetime

from mongoengine import *

from dashboard_server.application.repositories.mongo_repository import get_mongo_connection
from dashboard_server.domain.entities.ml_model import MlModel

db = get_mongo_connection()


class Worker(db.Document):
    meta = {"collection": "worker"}
    name = StringField(required=True)
    ts = DateTimeField(default=datetime.datetime.utcnow)
    host_name = StringField(required=True)
    host = StringField(required=True)
    model = ReferenceField(MlModel, default=None)
