# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Bluekiri V5 BigData Team <bigdata@bluekiri.com>.
#
# This program is free software: you can redistribute it and/or  modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# As a special exception, the copyright holders give permission to link the
# code of portions of this program with the OpenSSL library under certain
# conditions as described in each individual source file and distribute
# linked combinations including the program with the OpenSSL library. You
# must comply with the GNU Affero General Public License in all respects for
# all of the code used other than as permitted herein. If you modify file(s)
# with this exception, you may extend this exception to your version of the
# file(s), but you are not obligated to do so. If you do not wish to do so,
# delete this exception statement from your version. If you delete this
# exception statement from all source files in the program, then also delete
# it in the license file.

import os

# This variable is very important, this enroute the zookeeper path
PROJECT_SUFFIX = "-mlab"

PROJECT = "Demo" + PROJECT_SUFFIX

SERVICE_PORT = os.environ["PORT"]

# LDAP
LDAP_SERVER_URI = os.environ.get("LDAP_URI", "")
LDAP_BASE = os.environ.get("LDAP_BASE", "")
LDAP_DN = os.environ.get("LDAP_DN", "")
LDAP_PWD = os.environ.get("LDAP_PASS", "")
LDAP_EDIT_GROUPS = os.environ.get("LDAP_EDIT_GROUPS", "").split(',')
LDAP_GROUPS = LDAP_EDIT_GROUPS
# --------------------------------------------------------------------------------

# Mongo
MONGO_DATABASE = os.environ['DATABASE_NAME']
MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']
# --------------------------------------------------------------------------------

# Zookeeper
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']
# --------------------------------------------------------------------------------

CREATE_ADMIN_USER = os.environ.get("CREATE_ADMIN_USER", True)

# Flask
dashboard_home_title = os.environ["DASHBOARD_TITLE"]

flask_prefix = "dashboard"
flask_uri_prefix = "/" + flask_prefix

# Override your secret key
SECRET_KEY = os.environ.get("DASHBOARD_SECRET_KEY", "12345678901")

# Flask-Security config
SECURITY_URL_PREFIX = flask_uri_prefix
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT",
                                        "setyourcustompasswordsalthere")

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/users/"

SECURITY_POST_LOGIN_VIEW = flask_uri_prefix + "/"
SECURITY_POST_LOGOUT_VIEW = flask_uri_prefix + "/"

from dashboard.application.repositories.mongo_repository import \
    get_concat_mongo_uri

mongo_uri_with_database = get_concat_mongo_uri(MONGO_DATABASE,
                                               MONGO_CONNECTION_URI)

# db value only mean the project name... it doesn't make sense for me.
MONGODB_SETTINGS = {
    'db': MONGO_DATABASE,
    'host': mongo_uri_with_database
}
