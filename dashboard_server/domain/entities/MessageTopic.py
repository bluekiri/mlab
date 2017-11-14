# coding:utf-8
from dashboard_server.application.repositories.mongo_repository import get_mongo_connection

db = get_mongo_connection()


class MessageTopic(db.Document):
    name = db.StringField(primary_key=True)

    def __str__(self):
        return self.name
