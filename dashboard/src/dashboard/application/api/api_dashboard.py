from flask import Blueprint

from dashboard.application.api.model_api import register_model_methods
from dashboard.domain.interactor.mlmodel.create_ml_model import CreateMlModel
from dashboard.domain.interactor.users.token_verification import \
    TokenVerification
from dashboard.domain.repositories.worker_repository import WorkerRepository


class ApiDashboard:
    def __init__(self, token_verification: TokenVerification,
                 create_ml_model: CreateMlModel,
                 worker_repository: WorkerRepository):
        self.worker_repository = worker_repository
        self.create_ml_model = create_ml_model

        self.token_verification = token_verification

        self.api = Blueprint('api', __name__, url_prefix='/api')

        self.register_api_endpoints()

    def get_blueprint(self):
        return self.api

    def register_api_endpoints(self):
        register_model_methods(self.api, self.token_verification,
                               self.create_ml_model, self.worker_repository)
