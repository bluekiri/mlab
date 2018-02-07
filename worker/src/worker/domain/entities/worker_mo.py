import datetime

from mongoengine import *

from ...application.conf.config import MONGO_DATABASE
from ...application.conf.config import MONGO_CONNECTION_URI
from ...domain.entities.model_mo import Model

connect(db=MONGO_DATABASE, host=MONGO_CONNECTION_URI, connect=False)


class Worker(Document):
    meta = {"collection": "worker"}
    name = StringField(required=True)
    ts = DateTimeField(default=datetime.datetime.utcnow)
    host_name = StringField(required=True)
    host = StringField(required=True)
    model = ReferenceField(Model, default=None)
    group = StringField()
