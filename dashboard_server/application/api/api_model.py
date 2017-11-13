from datetime import datetime

from flask import Blueprint, request, make_response

from application.interactor.login.token_verification import is_valid_token
from dashboard_server.domain.entities.ml_model import MlModel

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/model', methods=('POST',))
def model():
    if not _is_valid_request_model():
        return make_response('Bad request', 400)
    token = request.args['token']
    if not is_valid_token(token):
        return "Invalid token", 401

    pickle = request.files['file']

    data = request.form
    name = data['name']

    description = ''
    if 'description' in data:
        description = data['description']

    MlModel(name=name, description=description, ts=datetime.now(), pickle=pickle).save()

    return make_response('Saved', 200)


def _is_valid_request_model():
    return 'token' in request.args and 'file' in request.files and 'name' in request.form
