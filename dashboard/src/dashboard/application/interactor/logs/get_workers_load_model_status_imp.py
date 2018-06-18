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

from dashboard.domain.interactor.logs.get_workers_load_model_status import \
    GetWorkersLoadModelStatus
from dashboard.domain.repositories.worker_repository import WorkerRepository


class GetWorkersLoadModelStatusImp(GetWorkersLoadModelStatus):
    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository

    def run(self):
        all_workers = self.worker_repository.get_available_workers()
        workers_state = {}
        for worker in all_workers:
            if not worker.up:
                self._append_or_create_items_in_dict(workers_state, "error",
                                                     worker)
            elif worker.model_loaded and worker.model_error:
                self._append_or_create_items_in_dict(workers_state, "warning",
                                                     worker)
            else:
                self._append_or_create_items_in_dict(workers_state, "success",
                                                     worker)
        return workers_state

    @staticmethod
    def _append_or_create_items_in_dict(dictionary, key, item):
        if key in dictionary.keys():
            dictionary[key].append(item)
        else:
            dictionary[key] = [item]
