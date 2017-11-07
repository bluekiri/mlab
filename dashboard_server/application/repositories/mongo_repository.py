from flask_mongoengine import MongoEngine

from dashboard_server.application.conf.config import mongo_connection_uri

_mongo_connection = None


def get_mongo_connection():
    global _mongo_connection
    if _mongo_connection is None:
        _mongo_connection = MongoEngine()
    return _mongo_connection
