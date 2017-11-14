import flask_admin
from flask import Blueprint, request
from flask_security import logout_user
from werkzeug.utils import redirect

from application.interactor.users.current_user_imp import CurrentUserImp
from dashboard_server.application.dashboard.views.api_token_view import ApiTokenView
from dashboard_server.application.dashboard.views.home_view import HomeView
from dashboard_server.application.dashboard.views.ml_model_publisher_view import \
    MLModelPublisherView
from dashboard_server.application.dashboard.views.ml_model_view import MlModelView
from dashboard_server.application.dashboard.views.user_admin_view import UserAdmin, RoleAdmin
from dashboard_server.application.interactor.orchestation.orchestation_interactor_imp import \
    OrchestationInteractorImp
from dashboard_server.application.interactor.users.user_messaging_imp import UserMessagingImp
from dashboard_server.application.interactor.users.users_privileges_imp import UsersPrivilegesImp
from dashboard_server.domain.entities.auth.api_token_model import Token
from dashboard_server.domain.entities.auth.login_model import User, Role
from dashboard_server.domain.entities.ml_model import MlModel

dashboard = Blueprint('dashboard', __name__, template_folder='templates', url_prefix='/dashboard')


@dashboard.route('/logout')
def logout_view():
    logout_user()
    return redirect(request.url_root + "dashboard/")


def init_admin(app):
    orchestation_interactor = OrchestationInteractorImp()
    users_privileges_interactor = UsersPrivilegesImp()
    current_user_interactor = CurrentUserImp()
    user_messaging = UserMessagingImp(current_user=current_user_interactor)
    app.jinja_env.globals.update(pending_messages=user_messaging.get_pending_messages)

    admin = flask_admin.Admin(app,
                              name='MLAB',
                              base_template='base.html',
                              index_view=HomeView(name="Dashboard", url=dashboard.url_prefix,
                                                  menu_icon_type='fa',
                                                  template='home.html',
                                                  menu_icon_value='fa-dashboard'),
                              category_icon_classes={
                                  'Access': 'glyphicon glyphicon-user',
                                  'PreProcess': 'glyphicon glyphicon-equalizer',

                              })

    # Add view
    admin.add_view(
        MlModelView(MlModel, name='Models', menu_icon_type='fa', menu_icon_value='fa-flask'))
    admin.add_view(UserAdmin(User, name='User', menu_icon_type='fa', menu_icon_value='fa-users'))
    admin.add_view(
        RoleAdmin(Role, name='Roles', menu_icon_type='fa', menu_icon_value='fa-address-book'))
    admin.add_view(
        ApiTokenView(Token, name='Api Token', menu_icon_type='fa', menu_icon_value='fa-key'))
    admin.add_view(MLModelPublisherView(name='Model publisher',
                                        users_privilages=users_privileges_interactor,
                                        orchestation_interactor=orchestation_interactor,
                                        menu_icon_type='fa', menu_icon_value='fa-desktop'))
