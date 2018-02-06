import inspect
import os

CURRENT_APPLICATION_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ASSETS_APPLICATION_PATH = CURRENT_APPLICATION_PATH + "/assets"
CONF_APPLICATION_PATH = CURRENT_APPLICATION_PATH + "/conf"

