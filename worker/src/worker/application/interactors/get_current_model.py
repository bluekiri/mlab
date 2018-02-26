from worker.domain.entities.logs_mo import Logs, LogsTopics
from worker.domain.repositories.model_repository import ModelRepository
from worker.domain.interactors.get_current_model import GetCurrentModel
from worker.domain.repositories.logs_repository import LogsRepository
from worker.domain.repositories.worker_repository import WorkerRepository


class GetCurrentModelImp(GetCurrentModel):
    def __init__(self, logs_repository: LogsRepository, worker_repository: WorkerRepository,
                 model_repository: ModelRepository):
        self.model_repository = model_repository
        self.worker_repository = worker_repository
        self.logs_repository = logs_repository

    def get_current_model(self):
        try:
            return self.model_repository.get_current_model()
        except Exception as e:
            log = Logs()
            log.topic = LogsTopics.worker_error.name
            log.text = "Error getting current model"
            self.logs_repository.save(log)
