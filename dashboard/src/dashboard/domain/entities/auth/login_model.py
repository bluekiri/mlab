from flask_security import RoleMixin
from flask_security import UserMixin

from dashboard.application.repositories.mongo_repository import get_mongo_connection

db = get_mongo_connection()


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    def __str__(self):
        return self.name


class User(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    name = db.StringField(max_length=255)
    username = db.StringField(max_length=255)
    password = db.StringField(required=False)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])
    topics = db.ListField(db.StringField(), default=[])

    def __str__(self):
        return self.name
