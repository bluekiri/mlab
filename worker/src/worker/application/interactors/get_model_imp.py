from worker.domain.entities.logs_mo import Logs, LogsTopics
from worker.domain.exception.unpickle_model_exception import UnpickleModelException
from worker.domain.interactors.send_mail import SendMail
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.interactors.get_model import GetModel
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class GetModelImp(GetModel):
    def __init__(self, logs_repository: LogsRepository, worker_repository: WorkerRepository,
                 model_repository: ModelRepository, send_mail: SendMail):
        self.send_mail = send_mail
        self.model_repository = model_repository
        self.worker_repository = worker_repository
        self.logs_repository = logs_repository

    def _build_success_load_model_log(self, model_name, model_id) -> Logs:
        log = Logs()
        log.topic = LogsTopics.activate_model.name
        log.text = "Model loaded successful"
        log.data = {"model_id": model_id,
                    "model_name": model_name,
                    "host": self.worker_repository.get_worker_host(),
                    "host_name": self.worker_repository.get_self_worker_model_id()}
        return log

    def _build_error_load_model_log(self, model_name, model_id) -> Logs:
        log = Logs()
        log.topic = LogsTopics.worker_error.name
        log.text = "Error getting current model"
        log.data = {"model_id": model_id,
                    "model_name": model_name,
                    "host": self.worker_repository.get_worker_host(),
                    "host_name": self.worker_repository.get_self_worker_model_id()}
        return log

    def get_current_model(self):
        global model
        model = None
        try:
            model = self.model_repository.get_current_model()
            if model is not None:
                log = self._build_success_load_model_log(model.name, model.pk)
                # self.logs_repository.save(log)
            self.worker_repository.set_success_model_load()
            return model
        except UnpickleModelException as e:
            if model is not None:
                log = self._build_error_load_model_log(model.name, model.pk)
                self.logs_repository.save(log)
            self.worker_repository.set_error_modal_load()

    def _send_model_error_alert(self, exception: Exception):
        self.send_mail.send_to_topic(LogsTopics.worker_error.name, str(exception), "Worker error")

    def switch_and_get_model_by_id(self, model_id):
        try:
            self.model_repository.try_load_new_model_instance(model_id)
            model = self.model_repository.get_current_model()
            self.worker_repository.set_success_model_load()
            return model
        except UnpickleModelException as e:
            log = self._build_error_load_model_log(self.model_repository.get_model_name_by_id(model_id), model_id)
            self.logs_repository.save(log)
            self.worker_repository.set_error_modal_load()
