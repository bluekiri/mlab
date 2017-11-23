import flask_admin
from flask import Blueprint, request
from flask import render_template
from flask_security import logout_user
from werkzeug.utils import redirect

from dashboard_server.application.dashboard.views.api_token_view import ApiTokenView
from dashboard_server.application.dashboard.views.home_view import HomeView
from dashboard_server.application.dashboard.views.logs_view import LogsView
from dashboard_server.application.dashboard.views.messages_view import MessageView
from dashboard_server.application.dashboard.views.ml_model_publisher_view import \
    MLModelPublisherView
from dashboard_server.application.dashboard.views.ml_model_view import MlModelView
from dashboard_server.application.dashboard.views.user_admin_view import UserAdmin, RoleAdmin
from dashboard_server.domain.entities.auth.api_token_model import Token
from dashboard_server.domain.entities.auth.login_model import User, Role
from dashboard_server.domain.entities.logs import Logs
from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.interactor.logs.get_time_line_events import GetTimeLineEvents
from dashboard_server.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor
from dashboard_server.domain.interactor.users.current_user import CurrentUser
from dashboard_server.domain.interactor.users.users_privileges import UsersPrivileges
from dashboard_server.domain.repositories.logs_repository import LogsRepository
from dashboard_server.domain.repositories.messages_repository import MessageRepository
from domain.interactor.logs.save_model_log_event import SaveModelLogEvent
from domain.interactor.messages.user_messaging import UserMessaging
from domain.repositories.model_repository import ModelRepository


class Dashboard:
    def __init__(self, app, model_repository: ModelRepository,
                 save_model_log_event: SaveModelLogEvent,
                 message_repository: MessageRepository, logs_repository: LogsRepository,
                 orchestation_interactor: OrchestationInteractor,
                 users_privileges: UsersPrivileges, current_user: CurrentUser,
                 user_messaging: UserMessaging, get_time_line_events: GetTimeLineEvents):
        self.model_repository = model_repository
        self.save_model_log_event = save_model_log_event
        self.get_time_line_events = get_time_line_events
        self.message_repository = message_repository
        self.current_user = current_user
        self.users_privileges = users_privileges
        self.orchestation_interactor = orchestation_interactor
        self.logs_repository = logs_repository
        self.user_messaging = user_messaging
        self.app = app

        self.dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates',
                                             url_prefix='/dashboard')

        app.jinja_env.globals.update(pending_messages=self.user_messaging.get_pending_messages)

        @self.dashboard_blueprint.route('/logout')
        def logout_view():
            logout_user()
            return redirect(request.url_root + "dashboard/")

        @self.app.errorhandler(404)
        def page_not_found(e):
            return render_template('404.html'), 404

        self._initialize_views()

    def get_blueprint(self):
        return self.dashboard_blueprint

    def _initialize_views(self):
        self.app.jinja_env.globals.update(pending_messages=self.user_messaging.get_pending_messages)

        admin = flask_admin.Admin(self.app,
                                  name='MLAB',
                                  base_template='base.html',
                                  index_view=HomeView(
                                      get_line_time_events=self.get_time_line_events,
                                      name="Dashboard", url=self.dashboard_blueprint.url_prefix,
                                      menu_icon_type='fa',
                                      template='home.html',
                                      menu_icon_value='fa-dashboard'),
                                  category_icon_classes={
                                      'Access': 'glyphicon glyphicon-user',
                                      'PreProcess': 'glyphicon glyphicon-equalizer',

                                  })

        # Add view
        admin.add_view(
            MlModelView(MlModel, model_repository=self.model_repository,
                        current_user=self.current_user,
                        save_model_log_event=self.save_model_log_event, name='Models',
                        menu_icon_type='fa', menu_icon_value='fa-flask'))
        admin.add_view(
            UserAdmin(User, name='User', menu_icon_type='fa', menu_icon_value='fa-users'))
        admin.add_view(
            RoleAdmin(Role, name='Roles', menu_icon_type='fa', menu_icon_value='fa-address-book'))
        admin.add_view(
            ApiTokenView(Token, name='Api Token', menu_icon_type='fa', menu_icon_value='fa-key'))
        admin.add_view(MLModelPublisherView(name='Model publisher',
                                            users_privilages=self.users_privileges,
                                            orchestation_interactor=self.orchestation_interactor,
                                            menu_icon_type='fa', menu_icon_value='fa-desktop'))
        admin.add_view(
            MessageView(name="Messages", menu_icon_type='fa', menu_icon_value='fa-inbox',
                        endpoint="messages", message_repository=self.message_repository,
                        user_messaging=self.user_messaging, current_user=self.current_user))

        admin.add_view(
            LogsView(Logs, current_user=self.current_user, name="Logs", menu_icon_type='fa',
                     menu_icon_value='fa-inbox'))
