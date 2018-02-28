import os

PROJECT_SUFFIX = "-mlab"
PROJECT = "Demo" + PROJECT_SUFFIX
SERVICE_PORT = os.environ['PORT']

# Mongodb
MONGO_DATABASE = os.environ['DATABASE_NAME']
MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']

# Zookeeper
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']

# Mail
SERVER_MAIL = os.environ.get("MLAB_MAIL_SERVER", "")
SERVER_FROM_USER = os.environ.get("NO_REPLY_USER", "")
SERVER_FROM_PASSWORD = os.environ.get("NO_REPLY_PASS", "")
