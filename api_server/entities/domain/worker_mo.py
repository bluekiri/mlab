import datetime

from mongoengine import *

from api_server.conf.config import mongo_connection_uri
from api_server.entities.domain.model_mo import Model

connect(host=mongo_connection_uri, connect=False)


class Worker(Document):
    meta = {"collection": "worker"}
    name = StringField(required=True)
    ts = DateTimeField(default=datetime.datetime.utcnow)
    host_name = StringField(required=True)
    host = StringField(required=True)
    model = ReferenceField(Model, default=None)
