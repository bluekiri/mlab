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

import datetime

from bson import ObjectId
from mongoengine import *

from dashboard.application.repositories.mongo_repository import \
    get_mongo_connection

db = get_mongo_connection()


class MlModel(db.Document):
    meta = {"collection": "mlmodel"}
    name = db.StringField(required=True)
    ts = db.DateTimeField(default=datetime.datetime.utcnow)
    description = db.StringField()
    extra_info = db.ListField(FileField())
    pickle = db.FileField(required=True)
    score = db.DecimalField(required=True, precision=5)
    classification_eval_file = db.FileField()

    def set_pk(self):
        self.pk = ObjectId()
        self._id = self.pk

    def __unicode__(self):
        return self.name
