# from web_service.models.auth.login_model import User
#
# from web_service.repositories.mongo_repository import get_mongo_connection
from dashboard.application.repositories.mongo_repository import get_mongo_connection
from dashboard.domain.entities.auth.login_model import User

db = get_mongo_connection()


class Token(db.Document):
    token = db.StringField()
    user = db.ReferenceField(User)
    description = db.StringField()
