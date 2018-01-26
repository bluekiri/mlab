from flask_mongoengine import MongoEngine

_mongo_connection = None


def get_mongo_connection():
    global _mongo_connection
    if _mongo_connection is None:
        _mongo_connection = MongoEngine()
    return _mongo_connection


def get_concat_mongo_uri(database, mongo_uri):
    import re
    match = re.match(r'(mongodb:\/\/[a-z:\._\-0-9]+)(\/.*)*', mongo_uri)
    slash_database = '/' + database
    if match is None or len(match.groups()) > 2:
        raise ConnectionError("Invalid mongo uri connection %s" % mongo_uri)
    match_groups = [item for item in match.groups() if item is not None]
    if len(match_groups) == 2:
        return slash_database.join(match_groups)
    return mongo_uri + slash_database
