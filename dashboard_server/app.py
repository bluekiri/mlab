#!/usr/bin/env python3

import inspect
import logging.config
import os
import sys

import flask_admin as admin
from flask import Flask
from flask_security import MongoEngineUserDatastore
from flask_security import Security

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dashboard_server.views.ml_model_publisher_view import MLModelPublisherView
from dashboard_server.views.user_admin_view import RoleAdmin, UserAdmin
from dashboard_server.views.forms.login_form import CustomLoginForm
from dashboard_server.conf.config import flask_uri_prefix, google_client_id
from dashboard_server import register_routes
from dashboard_server.auth.user import User, Role
from dashboard_server.models.ml_model import MlModel
from dashboard_server.repositories.mongo_repository import get_mongo_connection
from dashboard_server.views.home_view import HomeView
from dashboard_server.views.ml_model_view import MlModelView

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
conf_dir = os.path.join(currentdir, "conf")
logging.config.fileConfig(os.path.join(conf_dir, 'logging.ini'))

app = Flask(__name__)
app.config.from_pyfile(os.path.join(conf_dir, 'conf.py'))

# MongoDB settings
db = get_mongo_connection()
db.init_app(app)


@app.context_processor
def inject_globals():
    return dict(
        google_client_id=google_client_id,
    )


def init_security(_app):
    logging.info("Initialize security")
    user_datastore = MongoEngineUserDatastore(db, User, Role)
    Security(_app, user_datastore, login_form=CustomLoginForm)


init_security(app)
register_routes.register_routes(app)

admin = admin.Admin(app,
                    url=flask_uri_prefix,
                    name='Hotel booking probability',
                    template_mode='bootstrap3',
                    base_template='base.html',
                    index_view=HomeView(name="Dashboard", url=flask_uri_prefix, menu_icon_type='glyph',
                                        template='home.html', menu_icon_value='glyphicon-home'),
                    category_icon_classes={
                        'Access': 'glyphicon glyphicon-user',
                        'PreProcess': 'glyphicon glyphicon-equalizer',

                    })

# Add view
admin.add_view(MlModelView(MlModel, name='Models'))
admin.add_view(UserAdmin(User))
admin.add_view(RoleAdmin(Role))
admin.add_view(MLModelPublisherView(name='Model publisher'))

if __name__ == '__main__':
    # Start app
    app.run(debug=True, host='0.0.0.0', port=5000)
