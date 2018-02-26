# coding: utf-8


class WorkerRepository:

    def get_worker_host(self):
        raise NotImplementedError()

    def initialize_event_listener(self):
        raise NotImplementedError()

    def remove_worker_from_host(self, worker_name: str, host_name: str):
        raise NotImplementedError()

    def subscribe_on_worker_model_change(self, callback_function):
        raise NotImplementedError()

    def save_worker(self, number_of_instances: int):
        raise NotImplementedError()

    def get_self_worker_model_id(self) -> str:
        raise NotImplementedError()

    def success_model_load(self):
        raise NotImplementedError()

    def set_worker_model_error(self, error_log_id):
        raise NotImplementedError()
