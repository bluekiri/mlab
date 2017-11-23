# coding:utf-8
import datetime
from enum import Enum

from dateutil import tz

from dashboard_server.application.repositories.mongo_repository import get_mongo_connection
from dashboard_server.domain.entities.auth.login_model import User

db = get_mongo_connection()


class Topic(Enum):
    direct_message = "Direct Message"
    new_model = "New Model"


class SubjectData(Enum):
    welcome = {"icon": "fa-hand-spock-o", "text": "Hi %s, welcome to mlab."}
    direct_message = {"icon": "fa-envelope-open", "text": ""}
    new_model = {"icon": "fa-arrow-circle-o-up", "text": "Hey! a new mlmodel has been created."}


class Message(db.Document):
    ts = db.DateTimeField(default=datetime.datetime.utcnow)
    user = db.ReferenceField(User, default=None)
    subject_data = db.StringField()
    subject = db.StringField()
    text = db.StringField()
    topic = db.StringField()
    read_by = db.ListField(db.ReferenceField(User))
    # icon = ""

    def get_format_ts(self):
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        utc = self.ts.replace(tzinfo=from_zone)

        central = utc.astimezone(to_zone)
        diff_in_days = (datetime.datetime.utcnow().date() - self.ts.date()).days
        if diff_in_days > 0:
            return central.strftime(":%d, %b")
        return central.strftime("%H:%M")

    def __str__(self):
        return self.subject
