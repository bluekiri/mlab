# coding:utf-8
from flask import make_response
from flask import request

from dashboard.domain.interactor.mlmodel.create_ml_model import CreateMlModel
from dashboard.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor
from dashboard.domain.interactor.users.token_verification import \
    TokenVerification
from dashboard.domain.repositories.worker_repository import WorkerRepository


def register_model_methods(api, token_verification: TokenVerification,
                           create_ml_model: CreateMlModel,
                           worker_repository: WorkerRepository):
    @api.route('/mlmodel', methods=('POST',))
    def model():
        if not _is_valid_request_model():
            return make_response('Bad request', 400)
        token = request.args['token']

        if not token_verification.is_valid_token(token):
            return "Invalid token", 401

        pickle = request.files['file']

        data = request.form

        description = data['description'] if 'description' in data else ''

        model_id = create_ml_model.create(description=description,
                                          pickle=pickle,
                                          score=data['score'],
                                          creator_id=token, name=data['name'])
        _active_model_in_all_workers(str(model_id))
        return make_response('Ok', 200)

    def _active_model_in_all_workers(model_id):
        all_workers = worker_repository.get_available_workers()

        for worker in all_workers:
            if worker_repository.is_enable_auto_model_publication(
                    worker.host_name):
                worker_repository.set_model_in_worker(worker.host_name,
                                                      model_id)

    def _is_valid_request_model():
        return 'token' in request.args and 'file' in request.files and 'name' in request.form and 'score' in request.form
