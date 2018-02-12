import inspect
import os

CURRENT_APPLICATION_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_APPLICATION_PATH = os.path.abspath(os.path.join(CURRENT_APPLICATION_PATH, os.pardir))
STATIC_APPLICATION_PATH = PARENT_APPLICATION_PATH + "/static"
ASSETS_APPLICATION_PATH = CURRENT_APPLICATION_PATH + "/assets"
CONF_APPLICATION_PATH = CURRENT_APPLICATION_PATH + "/conf"


