import logging
import os
import socket

from api_server.entities.domain.model_mo import Model
from api_server.entities.domain.worker_mo import Worker

singleton_current_model = None
_loading_model = False


def get_current_model():
    global singleton_current_model
    if singleton_current_model is None:
        _load_default_model()
    return singleton_current_model


def _load_default_model():
    global singleton_current_model
    global _loading_model
    model = _get_model_for_this_host()
    if model is None:
        _loading_model = True
        try:
            singleton_current_model = Model.objects().first()
            singleton_current_model.get_model_instance()
        finally:
            _loading_model = False
        logging.info("Model not found... Loading first model (%s)" % singleton_current_model.name)
    else:
        try_load_new_model_instance()


def _get_model_for_this_host():
    pid_name = os.getpid()
    worker = Worker.objects(name=str(pid_name), host_name=socket.gethostname(),
                            host=socket.gethostbyname(socket.gethostname())).first()
    if worker is not None and worker.model is not None:
        return worker.model


def try_load_new_model_instance():
    model = _get_model_for_this_host()
    global singleton_current_model
    global _loading_model
    if model is None:
        return False
    if model.pk != singleton_current_model.pk and not _loading_model:
        logging.info("New model found (%s)" % model.name)
        model_found = Model.objects(pk=model.pk).first()
        _loading_model = True
        try:
            model_found.get_model_instance()
            singleton_current_model = model_found
        finally:
            _loading_model = False
        logging.info("New model loaded (%s)" % model.name)
        return True
    return False
