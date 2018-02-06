import os

PROJECT_SUFFIX = "-mlab"

PROJECT = "Demo" + PROJECT_SUFFIX
APP_NAME = "mlapiserver"

MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']
SERVICE_PORT = os.environ['PORT']
