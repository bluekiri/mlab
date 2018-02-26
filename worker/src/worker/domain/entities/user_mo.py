from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField, ListField

class Role(Document):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)

    def __str__(self):
        return self.name

class User(Document):
    email = StringField(max_length=255)
    name = StringField(max_length=255)
    username = StringField(max_length=255)
    password = StringField(required=False)
    active = BooleanField(default=True)
    confirmed_at = DateTimeField()
    roles = ListField(ReferenceField(Role), default=[])
    topics = ListField(StringField(), default=[])

    def __str__(self):
        return self.name