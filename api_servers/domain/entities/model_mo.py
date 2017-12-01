import logging

import dill as pkl
from mongoengine import *

from api_servers.application.conf.config import MONGO_CONNECTION_URI

connect(host=MONGO_CONNECTION_URI, connect=False)
logger = logging.getLogger()


class Model(Document):
    meta = {"collection": "mlmodel", "strict": False}
    name = StringField(required=True)
    deserialized_model_instance = None
    pickle = FileField(required=True)

    def get_model_instance(self):
        if self.deserialized_model_instance is None:
            content = self.pickle.read()
            self.deserialized_model_instance = pkl.loads(content)
        return self.deserialized_model_instance
