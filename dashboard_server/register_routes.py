from flask import Response
from flask import request
from flask import url_for
from flask_security import login_user
from flask_security import logout_user
from werkzeug.utils import redirect

from dashboard_server.conf.config import flask_uri_prefix
from dashboard_server.interactor.login.login_verification import get_user_from_username
from dashboard_server.repositories.google_api_repository import is_sig_in_outh_token_verificated, get_mail_from_token


def register_routes(app):
    @app.route(flask_uri_prefix + '/login/g_auth', methods=('GET',))
    def login_g_auth():
        g_token = request.args.get('token')
        if is_sig_in_outh_token_verificated(g_token):
            username = get_mail_from_token(g_token)
            user = get_user_from_username(username)
            user.save()
            login_user(user)
            return redirect(url_for('admin.index'))

        return Response('Denied_access', 401,
                        {'WWWAuthenticate': 'Basic realm="Login Required"'})

    @app.route(flask_uri_prefix + '/logout/')
    def logout_view():
        logout_user()
        sing_out_url = "https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=" + request.url_root + "hbp_dashboard/login"
        return redirect(sing_out_url)
