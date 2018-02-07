# coding:utf-8
import datetime
import json
from typing import List

from dashboard.application.conf.config import PROJECT
from dashboard.application.datasource.zk_datasource_imp import ZKDatasourceImp
from dashboard.domain.entities.worker_mo import Worker
from dashboard.domain.repositories.model_repository import ModelRepository
from dashboard.domain.repositories.worker_repository import WorkerRepository


class WorkerRepositoryImp(WorkerRepository):
    workers_path = "/%s/workers" % PROJECT

    def __init__(self, zk_datasource: ZKDatasourceImp, model_repository: ModelRepository):
        self.model_resitory = model_repository
        self.zk_datasource = zk_datasource
        self.worker_down_callbacks = []

        # @self.zk_datasource.zk.ChildrenWatch(self.workers_path)
        # def watch_children(children):
        #     print("Children are now: %s" % children)
        #     for callback in self.worker_down_callbacks:
        #         callback(children)

    def subscribe_worker_down_callback(self, callback):
        self.worker_down_callbacks.append(callback)

    def get_available_workers(self) -> List[Worker]:
        workers = []
        if self.zk_datasource.zk.exists(self.workers_path) is not None:
            workers_info = self.zk_datasource.zk.get_children(self.workers_path)
            for worker_info in workers_info:
                znode_worker = self.zk_datasource.zk.get("%s/%s" % (self.workers_path, worker_info))
                worker_data = json.loads(znode_worker[0].decode('utf-8'))
                ts = datetime.datetime.fromtimestamp(znode_worker[1].created)
                is_up = False
                if self.zk_datasource.zk.exists("%s/%s/up" % (self.workers_path, worker_info)):
                    is_up = True
                    znode_up = self.zk_datasource.zk.get(
                        "%s/%s/up" % (self.workers_path, worker_info))
                    ts = datetime.datetime.fromtimestamp(znode_up[1].created)

                worker = Worker(host_name=worker_info, host=worker_data["host"],
                                number_of_instances=worker_data["instances"],
                                model=self.model_resitory.get_model_by_id(
                                    self._get_model_for_worker(worker_info)),
                                group=self._get_group_for_worker(worker_info),
                                ts=ts,
                                up=is_up)
                workers.append(worker)
        return workers

    def get_groups(self):
        return list(set(
            [worker.group for worker in self.get_available_workers() if worker.group is not None]))

    def get_workers_host_by_group(self, group: str) -> List[str]:
        workers_info = self.zk_datasource.zk.get_children(self.workers_path)
        return [worker_info for worker_info in workers_info if
                self._get_group_for_worker(worker_info) == group]

    def set_group_in_worker(self, worker_host: str, group: str):
        self.zk_datasource.update_or_create("%s/%s" % (self.workers_path, worker_host), "group",
                                            group)

    def set_model_in_worker(self, worker_host: str, model_id: str):
        self.zk_datasource.update_or_create("%s/%s" % (self.workers_path, worker_host), "model",
                                            model_id)

    def _get_group_for_worker(self, worker_host):
        group_path = "%s/%s/group" % (self.workers_path, worker_host)
        if self.zk_datasource.zk.exists(group_path) is not None:
            return self.zk_datasource.zk.get(group_path)[0].decode('utf-8')

    def _get_model_for_worker(self, worker_host):
        model_path = "%s/%s/model" % (self.workers_path, worker_host)
        if self.zk_datasource.zk.exists(model_path) is not None:
            return self.zk_datasource.zk.get(model_path)[0].decode('utf-8')
