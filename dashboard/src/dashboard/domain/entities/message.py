# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Bluekiri V5 BigData Team <bigdata@bluekiri.com>.
#
# This program is free software: you can redistribute it and/or  modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# As a special exception, the copyright holders give permission to link the
# code of portions of this program with the OpenSSL library under certain
# conditions as described in each individual source file and distribute
# linked combinations including the program with the OpenSSL library. You
# must comply with the GNU Affero General Public License in all respects for
# all of the code used other than as permitted herein. If you modify file(s)
# with this exception, you may extend this exception to your version of the
# file(s), but you are not obligated to do so. If you do not wish to do so,
# delete this exception statement from your version. If you delete this
# exception statement from all source files in the program, then also delete
# it in the license file.

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
