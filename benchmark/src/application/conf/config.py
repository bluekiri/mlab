import os

SERVICE_PORT = os.environ['PORT']

# Zookeeper
PROJECT_SUFFIX = "-mlab"
PROJECT = "Demo" + PROJECT_SUFFIX
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']

# Mongo
MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']

