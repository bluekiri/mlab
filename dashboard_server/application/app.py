#!/usr/bin/env python3

import logging.config
import os

import yaml
from flask import Flask
from flask_security import MongoEngineUserDatastore
from flask_security import Security

from dashboard_server.application.api.api_dashboard import ApiDashboard
from dashboard_server.application.dashboard.dashboard_initialize import Dashboard
from dashboard_server.application.dashboard.views.forms.login_form import CustomLoginForm
from dashboard_server.application.interactor.logs.get_time_line_events_imp import \
    GetTimeLineEventsImp
from dashboard_server.application.interactor.logs.save_model_log_event_imp import \
    SaveModelModelLogEventImp
from dashboard_server.application.interactor.messages.send_message_imp import SendMessageImp
from dashboard_server.application.interactor.mlmodel.create_ml_model_imp import CreateMlModelImp
from dashboard_server.application.interactor.orchestation.orchestation_interactor_imp import \
    OrchestationInteractorImp
from dashboard_server.application.interactor.users.current_user_imp import CurrentUserImp
from dashboard_server.application.interactor.users.token_verification import TokenVerificationImp
from dashboard_server.application.interactor.users.user_messaging_imp import UserMessagingImp
from dashboard_server.application.interactor.users.users_privileges_imp import UsersPrivilegesImp
from dashboard_server.application.repositories.logs_repository_imp import LogsRepositoryImp
from dashboard_server.application.repositories.message_repository_imp import MessageRepositoryImp
from dashboard_server.application.repositories.model_repository_imp import ModelRepositoryImp
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

# Dependencies
message_repository = MessageRepositoryImp()
logs_repository = LogsRepositoryImp()
model_repository = ModelRepositoryImp()

token_verification = TokenVerificationImp()
orchestation_interactor = OrchestationInteractorImp()
users_privileges = UsersPrivilegesImp()
current_user = CurrentUserImp()
user_messaging = UserMessagingImp(current_user=current_user,
                                  message_repository=message_repository)
get_time_line_events = GetTimeLineEventsImp(logs_repository)
save_model_log_event = SaveModelModelLogEventImp(current_user=current_user,
                                                 log_repository=logs_repository)
send_message = SendMessageImp(message_repository)
create_ml_model = CreateMlModelImp(send_message=send_message,
                                   save_model_log_event=save_model_log_event,
                                   model_repository=model_repository)

# Blueprints
dashboard = Dashboard(app=app, model_repository=model_repository,
                      save_model_log_event=save_model_log_event,
                      message_repository=message_repository,
                      logs_repository=logs_repository, current_user=current_user,
                      orchestation_interactor=orchestation_interactor,
                      get_time_line_events=get_time_line_events, user_messaging=user_messaging,
                      users_privileges=users_privileges)

app.register_blueprint(dashboard.get_blueprint())

api_dashboard = ApiDashboard(create_ml_model=create_ml_model,
                             token_verification=token_verification)

app.register_blueprint(api_dashboard.get_blueprint())

# This snippet of code is user with password create example
# with app.app_context():
#     admin_role = user_datastore.find_or_create_role('admin')
#     user_datastore.create_user(email='admin', password=utils.hash_password('admin'), name='admin',
#                                username='admin', roles=[admin_role])

if __name__ == '__main__':
    # Start app
    app.run(debug=True, host='0.0.0.0', port=5000)
