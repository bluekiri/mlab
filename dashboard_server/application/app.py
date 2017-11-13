#!/usr/bin/env python3

import logging.config
import os

import yaml
from flask import Flask
from flask_security import MongoEngineUserDatastore
from flask_security import Security

from dashboard_server.application.api.api_model import api
from dashboard_server.application.dashboard.profile import dashboard
from dashboard_server.application.dashboard.profile import init_admin
from dashboard_server.application.dashboard.views.forms.login_form import CustomLoginForm
from dashboard_server.application.repositories.mongo_repository import get_mongo_connection
from dashboard_server.application.util import CONF_APPLICATION_PATH, CURRENT_APPLICATION_PATH
from dashboard_server.domain.entities.auth.login_model import User, Role


def setup_logging(default_path=CONF_APPLICATION_PATH, default_level=logging.INFO,
                  env_key='API-SERVER'):
    path = default_path + '/logging.yaml'
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    return logging.getLogger(__name__)


app = Flask(__name__)
app.config.from_pyfile(os.path.join(CONF_APPLICATION_PATH, 'config.py'))
app.template_folder = CURRENT_APPLICATION_PATH + "/dashboard/templates"
app.static_folder = CURRENT_APPLICATION_PATH + "/dashboard/static"

# MongoDB settings
db = get_mongo_connection()
db.init_app(app)

logging.info("Initialize security")
user_datastore = MongoEngineUserDatastore(db, User, Role)
Security(app, user_datastore, login_form=CustomLoginForm)
init_admin(app)
app.register_blueprint(dashboard)
app.register_blueprint(api)

# This snippet of code is user with password create example
# with app.app_context():
#     admin_role = user_datastore.find_or_create_role('admin')
#     user_datastore.create_user(email='admin', password=utils.hash_password('admin'), name='admin',
#                                username='admin', roles=[admin_role])

if __name__ == '__main__':
    # Start app
    app.run(debug=True, host='0.0.0.0', port=5000)
