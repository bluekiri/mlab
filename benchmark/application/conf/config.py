import os

PROJECT_SUFFIX="-mlab"

PROJECT = "Demo"+PROJECT_SUFFIX
MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']
APP_NAME = "ml_api_server"
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']
