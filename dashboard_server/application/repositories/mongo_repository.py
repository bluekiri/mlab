from flask_mongoengine import MongoEngine

_mongo_connection = None


def get_mongo_connection():
    global _mongo_connection
    if _mongo_connection is None:
        _mongo_connection = MongoEngine()
    return _mongo_connection
