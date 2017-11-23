import datetime

from bson import ObjectId
from mongoengine import *

from dashboard_server.application.repositories.mongo_repository import get_mongo_connection

db = get_mongo_connection()


class MlModel(db.Document):
    meta = {"collection": "mlmodel"}
    name = db.StringField(required=True)
    ts = db.DateTimeField(default=datetime.datetime.utcnow)
    description = db.StringField()
    extra_info = db.ListField(FileField())
    pickle = db.FileField(required=True)
    score = db.DecimalField(required=True)
    classification_eval_file = db.FileField()

    def set_pk(self):
        self.pk = ObjectId()
        self._id = self.pk

    def __unicode__(self):
        return self.name
