import redis

from dashboard_server.conf.config import redis_connection_uri, redis_database

_redis_connection = None


def get_redis_connection():
    global _redis_connection
    if _redis_connection is None:
        _redis_connection = redis.StrictRedis(host=redis_connection_uri, port=6379, db=redis_database)
    return _redis_connection
