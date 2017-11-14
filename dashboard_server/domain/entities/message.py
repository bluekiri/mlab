# coding:utf-8
import datetime
from enum import Enum

from dashboard_server.application.repositories.mongo_repository import get_mongo_connection

db = get_mongo_connection()


class Topic(Enum):
    NewModel = "New model"


class Message(db.Document):
    ts = db.DateTimeField(default=datetime.datetime.utcnow)
    subject = db.StringField()
    text = db.StringField()
    topic = db.StringField()

    def get_format_ts(self):
        diff_in_days = (datetime.datetime.utcnow().date() - self.ts.date()).days
        if diff_in_days > 0:
            return self.ts.strftime(":%d, %b")
        return self.ts.strftime("%H:%M")

    def __str__(self):
        return self.subject
