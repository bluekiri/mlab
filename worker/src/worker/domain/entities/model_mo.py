# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import logging

import dill as pkl
from mongoengine import *

from worker.application.conf.config import MONGO_CONNECTION_URI, MONGO_DATABASE

connect(host=MONGO_CONNECTION_URI, db=MONGO_DATABASE, connect=False)
logger = logging.getLogger()


class Model(Document):
    meta = {"collection": "mlmodel", "strict": False}
    name = StringField(required=True)
    deserialized_model_instance = None
    pickle = FileField(required=True)

    def get_model_instance(self):
        pkl.dill._reverse_typemap['ClassType'] = type
        if self.deserialized_model_instance is None:
            content = self.pickle.read()
            self.deserialized_model_instance = pkl.loads(content)
        return self.deserialized_model_instance
