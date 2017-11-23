from flask import Blueprint

from dashboard_server.application.api.model_api import register_model_methods
from dashboard_server.domain.interactor.mlmodel.create_ml_model import CreateMlModel
from dashboard_server.domain.interactor.users.token_verification import TokenVerification


class ApiDashboard:
    def __init__(self, token_verification: TokenVerification,
                 create_ml_model: CreateMlModel):
        self.create_ml_model = create_ml_model
        self.token_verification = token_verification

        self.api = Blueprint('api', __name__, url_prefix='/api')

        self.register_api_endpoints()

    def get_blueprint(self):
        return self.api

    def register_api_endpoints(self):
        register_model_methods(self.api, self.token_verification, self.create_ml_model)
