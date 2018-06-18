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

from dashboard.domain.entities.logs import LogsTopics
from dashboard.domain.repositories.logs_repository import LogsRepository
from dashboard.domain.interactor.logs.get_time_line_events import \
    GetTimeLineEvents


class GetTimeLineEventsImp(GetTimeLineEvents):
    def __init__(self, logs_repository: LogsRepository):
        self.logs_repository = logs_repository

    def get_all_time_events(self):
        return self.logs_repository.get_logs_by_topics(
            [LogsTopics.new_model.name])
        # log.ts = log.ts.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
