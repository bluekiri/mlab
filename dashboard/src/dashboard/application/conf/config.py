import os

# This variable is very important, this enroute the zookeeper path
PROJECT_SUFFIX = "-mlab"

PROJECT = "Demo" + PROJECT_SUFFIX

SERVICE_PORT = os.environ["PORT"]

# LDAP
LDAP_SERVER_URI = os.environ["LDAP_URI"]
LDAP_BASE = os.environ.get("LDAP_BASE")
LDAP_DN = os.environ.get("LDAP_DN")
LDAP_PWD = os.environ.get("LDAP_PASS")
LDAP_EDIT_GROUPS = os.environ.get("LDAP_EDIT_GROUPS", []).split(',')
LDAP_GROUPS = LDAP_EDIT_GROUPS
# --------------------------------------------------------------------------------

# Mongo
MONGO_DATABASE = os.environ['DATABASE_NAME']
MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']
# --------------------------------------------------------------------------------

# Zookeeper
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']
# --------------------------------------------------------------------------------

# Flask
dashboard_home_title = os.environ["DASHBOARD_TITLE"]

flask_prefix = "dashboard"
flask_uri_prefix = "/" + flask_prefix

# Override your secret key
SECRET_KEY = os.environ.get("DASHBOARD_SECRET_KEY", "12345678901")

# Flask-Security config
SECURITY_URL_PREFIX = flask_uri_prefix
SECURITY_PASSWORD_HASH = os.environ.get("SECURITY_PASSWORD_HASH",
                                        "abcde1_sha512")
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
