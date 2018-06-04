from worker.domain.entities.logs_mo import Logs, LogsTopics
from worker.domain.exception.unpickle_model_exception import UnpickleModelException
from worker.domain.interactors.send_mail import SendMail
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.interactors.get_model import GetModel
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class GetModelImp(GetModel):
    def __init__(self, logs_repository: LogsRepository,
                 worker_repository: WorkerRepository,
                 model_repository: ModelRepository, send_mail: SendMail):
        self.send_mail = send_mail
        self.model_repository = model_repository
        self.worker_repository = worker_repository
        self.logs_repository = logs_repository

    def get_current_model(self):
        global model
        model = None
        try:
            model = self.model_repository.get_current_model()
            return model
        except UnpickleModelException as e:
            self.worker_repository.set_error_modal_load()
            self._send_model_error_alert(e)

    def _send_model_error_alert(self, exception: Exception):
        self.send_mail.send_to_topic(LogsTopics.worker_error.name, str(exception),
                                     "Worker error")

    def switch_and_get_model_by_id(self, model_id):
        try:
            self.model_repository.try_load_new_model_instance(model_id)
            return self.model_repository.get_current_model()
        except UnpickleModelException as e:
            self._send_model_error_alert(e)
            self.worker_repository.set_error_modal_load()
