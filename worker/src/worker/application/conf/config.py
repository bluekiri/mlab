import os

PROJECT_SUFFIX = "-mlab"
PROJECT = "Demo" + PROJECT_SUFFIX
SERVICE_PORT = os.environ['PORT']

# Mongodb
MONGO_DATABASE = os.environ['DATABASE_NAME']
MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']

# Zookeeper
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']
