from flask import Blueprint, request, flash, make_response

from dashboard_server.domain.entities.auth.api_token_model import Token
from dashboard_server.domain.entities.ml_model import MlModel

api = Blueprint('api', __name__, url_prefix='/api')


def is_valid_token(token):
    try:
        t = Token.objects(token=token)
        if not t:
            return False

        return True
    except ValueError:
        return False


@api.route('/model', methods=('POST',))
def model():
    if 'token' in request.args:
        token = request.args['token']

        if is_valid_token(token):
            if 'file' not in request.files:
                flash('No file part')
                return 'No'

            pickle = request.files['file']

            data = request.form
            name = data['name']

            description = ''
            if 'description' in data:
                description = data['description']

            model = MlModel(name=name, description=description, pickle=pickle)
            model.save()

            return make_response('Done', 200)
        else:
            return make_response('Not valid token', 200)
    else:
        return "No token specified"
