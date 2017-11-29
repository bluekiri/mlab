# coding: utf-8
import json
import logging
import socket
from datetime import datetime

from api_servers.domain.repositories.worker_repository import WorkerRepository


class WorkerRepositoryImp(WorkerRepository):
    def __init__(self, zk_datasource):
        self.zk_datasource = zk_datasource
        self.logger = logging.getLogger(__name__)
        self.host_name = socket.gethostbyname(socket.gethostname())
        self.worker_path = "/workers/" + self.host_name
        self.model_change_callbacks = []

    def initialize_event_listener(self):
        @self.zk_datasource.zk.DataWatch(self.worker_path + "/model")
        def watch_node(data, stat):
            for callback in self.model_change_callbacks:
                callback(data)

    def subscribe_on_worker_model_change(self, callback_function):
        self.model_change_callbacks.append(callback_function)

    def remove_worker_from_host(self, worker_name: str, host_name: str):
        pass

    def save_worker(self, number_of_instances: int):
        data = json.dumps(
            {"host": socket.gethostname(), "instances": number_of_instances})

        if self.zk_datasource.zk.exists(self.worker_path) is not None:
            pass
        else:
            self.zk_datasource.zk.ensure_path(self.worker_path)
            self.zk_datasource.zk.create(self.worker_path, data.encode('utf-8'))

        try:
            self.zk_datasource.zk.create(self.worker_path + "/up",
                                         str(datetime.utcnow().timestamp()).encode('utf-8'),
                                         ephemeral=True)
        except:
            self.logger.info("Worker reload")
