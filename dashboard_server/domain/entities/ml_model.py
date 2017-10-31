import datetime

from mongoengine import *

from dashboard_server.application.repositories.mongo_repository import get_mongo_connection

db = get_mongo_connection()


class MlModel(db.Document):
    meta = {"collection": "model"}
    name = db.StringField(required=True)
    ts = db.DateTimeField(default=datetime.datetime.utcnow)
    description = db.StringField()
    extra_info = db.ListField(FileField())
    pickle = db.FileField(required=True)

    def __unicode__(self):
        return self.name
