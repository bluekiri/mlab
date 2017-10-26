import threading

from api_server.repository.mongo.model_repository import get_current_model, try_load_new_model_instance


def active_listener():
    threading.Timer(5.0, active_listener).start()
    try_load_new_model_instance()
