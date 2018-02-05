# coding:utf-8
from flask import make_response
from flask import request

from domain.interactor.mlmodel.create_ml_model import CreateMlModel
from domain.interactor.users.token_verification import TokenVerification


def register_model_methods(api, token_verification: TokenVerification,
                           create_ml_model: CreateMlModel):
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

        create_ml_model.create(description=description, pickle=pickle, score=data['score'],
                               creator_id=token, name=data['name'])

        return make_response('Ok', 200)

    def _is_valid_request_model():
        return 'token' in request.args and 'file' in request.files and 'name' in request.form
