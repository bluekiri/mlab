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
from typing import Dict

import timeago

from dashboard.application.conf.config import WORKER_PORT
from dashboard.domain.entities.worker import Worker
from dashboard.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor
from dashboard.domain.repositories.worker_repository import WorkerRepository


class OrchestationInteractorImp(OrchestationInteractor):

    def __init__(self, worker_repository: WorkerRepository):
        self.worker_repository = worker_repository

    def load_model_on_group(self, group: str, model_id: str):
        workers_host = self.worker_repository.get_workers_host_by_group(group)
        for worker_host in workers_host:
            self.worker_repository.set_model_in_worker(worker_host, model_id)

    def set_group_to_worker(self, host_id: str, group_name: str):
        self.worker_repository.set_group_in_worker(host_id, group_name)

    def _get_workers_grouped(self):

        def _map_worker_to_dict(worker: Worker) -> Dict:
            return {
                "hostname": worker.host_name,
                "swagger_uri": "http://%s:%s" % (worker.host, str(WORKER_PORT)),
                "worker": worker.number_of_instances,
                "ts": timeago.format(worker.ts, datetime.datetime.utcnow()),
                "model_name": "Model not loaded" if worker.model is None else worker.model.name + " - " + str(
                    worker.model.ts),
                "group": worker.group,
                "running": worker.up,
                "auto_model_publisher": worker.auto_model_publisher
            }

        workers = self.worker_repository.get_available_workers()

        return [_map_worker_to_dict(worker) for worker in workers]

    def get_group_workers(self):
        groups = {}
        without_group = []
        clusters = self._get_workers_grouped()
        for cluster in clusters:
            if cluster["group"] is None:
                without_group.append(cluster)
            elif cluster["group"] in groups.keys():
                groups[cluster["group"]].append(cluster)
            else:
                groups[cluster["group"]] = [cluster]
        return groups, without_group

    def load_model_on_host(self, host, model_id):
        self.worker_repository.set_model_in_worker(worker_host=host,
                                                   model_id=model_id)

    def set_auto_model_publisher(self, host: str, enable: bool):
        self.worker_repository.set_auto_model_publisher(worker_host=host,
                                                        enable=enable)

    def get_groups(self):
        return self.worker_repository.get_groups()

    def remove_disconnected_worker(self, worker_host: str):
        available_workers = self.worker_repository.get_available_workers()
        if worker_host not in [worker.host_name for worker in
                               available_workers if worker.up]:
            self.worker_repository.remove_worker(worker_host)
