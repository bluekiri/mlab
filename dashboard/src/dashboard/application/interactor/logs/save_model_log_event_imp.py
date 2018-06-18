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
from typing import List

from dashboard.domain.entities.logs import Logs, LogsTopics
from dashboard.domain.interactor.logs.save_model_log_event import SaveModelLogEvent
from dashboard.domain.interactor.users.current_user import CurrentUser
from dashboard.domain.repositories.logs_repository import LogsRepository


class SaveModelModelLogEventImp(SaveModelLogEvent):
    def __init__(self, log_repository: LogsRepository, current_user: CurrentUser):
        self.current_user = current_user
        self.log_repository = log_repository

    def _get_empty_log_event(self, topic: LogsTopics, model_name: str, model_id: str,
                             is_system_event: bool, source_id: str = None):
        log = Logs()
        log.ts = datetime.datetime.utcnow()
        log.topic = topic.name
        log.data = {
            "model_name": model_name,
            "model_id": model_id,
        }

        if is_system_event:
            return log

        log.source_id = str(
            self.current_user.get_current_user().pk) if source_id is None else str(source_id)

        return log

    def save_new_model_event(self, model_name: str, model_id: str, is_system_event: bool,
                             source_id: str):
        log = self._get_empty_log_event(LogsTopics.new_model, model_name, model_id, is_system_event,
                                        source_id)
        self.log_repository.save(log)

    def save_activate_model_by_group_event(self, model_name: str, model_id: str, host: List[str],
                                           group_name: str, is_system_event: bool, source_id: str):
        log = self._get_empty_log_event(LogsTopics.activate_model, model_name, model_id, is_system_event,
                                        source_id)
        log.data["host"] = host
        log.data["group"] = group_name
        self.log_repository.save(log)

    def save_activate_model_event(self, model_name: str, model_id: str, host: List[str],
                                  is_system_event: bool, source_id: str):
        log = self._get_empty_log_event(LogsTopics.activate_model, model_name, model_id, is_system_event,
                                        source_id)
        log.data["host"] = host

        self.log_repository.save(log)
