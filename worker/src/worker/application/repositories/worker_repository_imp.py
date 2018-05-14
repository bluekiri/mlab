# coding: utf-8
import json
import logging
import socket
from datetime import datetime

from worker.domain.repositories.worker_repository import WorkerRepository
from worker.application.conf.config import PROJECT


class WorkerRepositoryImp(WorkerRepository):
    def __init__(self, zk_datasource):
        self.zk_datasource = zk_datasource
        self.logger = logging.getLogger(__name__)
        self.host_name = socket.gethostname()
        self.host = socket.gethostbyname(socket.gethostname())
        self.workers_path = "/%s/workers" % PROJECT
        self.worker_path = "%s/%s" % (self.workers_path, self.host_name)
        self.model_change_callbacks = []

    def get_worker_host(self):
        return self.host

    def get_self_worker_model_id(self) -> str:
        if self.zk_datasource.zk.exists(self.worker_path + "/model"):
            return self.zk_datasource.zk.get(self.worker_path + "/model")[0].decode(
                "utf-8")

    def initialize_event_listener(self):
        @self.zk_datasource.zk.DataWatch(self.worker_path + "/model")
        def watch_node(data, stat):
            for callback in self.model_change_callbacks:
                callback(data.decode('utf-8'))

    def subscribe_on_worker_model_change(self, callback_function):
        self.model_change_callbacks.append(callback_function)

    def remove_worker_from_host(self, worker_name: str, host_name: str):
        pass

    def save_worker(self, number_of_instances: int):
        data = json.dumps(
            {"host": self.host, "instances": number_of_instances})

        if self.zk_datasource.zk.exists(self.worker_path) is not None:
            self.zk_datasource.zk.set(self.worker_path, data.encode('utf-8'))
        else:
            self.zk_datasource.zk.ensure_path(self.workers_path)
            self.zk_datasource.zk.create(self.worker_path, data.encode('utf-8'))

        try:
            self.zk_datasource.zk.create(self.worker_path + "/up",
                                         str(datetime.utcnow().timestamp()).encode(
                                             'utf-8'), ephemeral=True)
        except:
            self.logger.info("Worker reload")

    def is_current_worker_loaded_on_zoo(self):
        return self.zk_datasource.zk.exists(self.worker_path + "/up") is not None

    def set_success_model_load(self):
        if self.zk_datasource.zk.exists(self.worker_path) is not None:
            data = json.loads(
                self.zk_datasource.zk.get(self.worker_path)[0].decode("utf-8"))
            if "model_error" in data:
                del data["model_error"]
                data["model_success"] = str(datetime.now())
                self.zk_datasource.zk.set(self.worker_path,
                                          json.dumps(data).encode('utf-8'))

    def set_error_modal_load(self):
        if self.zk_datasource.zk.exists(self.worker_path) is not None:
            data = json.loads(
                self.zk_datasource.zk.get(self.worker_path)[0].decode("utf-8"))
            data["model_error"] = str(datetime.now())
            self.zk_datasource.zk.set(self.worker_path, json.dumps(data).encode('utf-8'))
