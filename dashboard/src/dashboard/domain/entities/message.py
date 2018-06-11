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
from enum import Enum

from dateutil import tz

from dashboard.application.repositories.mongo_repository import get_mongo_connection
from dashboard.domain.entities.auth.login_model import User

db = get_mongo_connection()


class Topic(Enum):
    direct_message = "Direct Message"
    new_model = "New Model"


class SubjectData(Enum):
    welcome = {"icon": "fa-hand-spock-o", "text": "Hi %s, welcome to mlab."}
    direct_message = {"icon": "fa-envelope-open", "text": ""}
    new_model = {"icon": "fa-arrow-circle-o-up", "text": "Hey! New mlmodel created."}


class Message(db.Document):
    ts = db.DateTimeField(default=datetime.datetime.utcnow)
    user = db.ReferenceField(User, default=None)
    subject_data = db.StringField()
    subject = db.StringField()
    text = db.StringField()
    topic = db.StringField()
    read_by = db.ListField(db.ReferenceField(User))

    # icon = ""

    def get_format_ts(self):
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        utc = self.ts.replace(tzinfo=from_zone)

        central = utc.astimezone(to_zone)
        diff_in_days = (datetime.datetime.utcnow().date() - self.ts.date()).days
        if diff_in_days > 0:
            return central.strftime(":%d, %b")
        return central.strftime("%H:%M")

    def __str__(self):
        return self.subject
