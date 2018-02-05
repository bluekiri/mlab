import os

# This variable is very important, this enroute the zookeeper path

PROJECT_SUFFIX = "-mlab"

PROJECT = "Demo" + PROJECT_SUFFIX

# LDAP
ldap_server = os.environ["LDAP_URI"]
ldap_base = "***REMOVED***"
ldap_dn = "***REMOVED***"
ldap_pwd = "***REMOVED***"
ldap_edit_groups = ['***REMOVED***']
ldap_groups = ['***REMOVED***']
# --------------------------------------------------------------------------------

# Mongo
mongo_database = os.environ['DATABASE_NAME']
mongo_connection_uri = os.environ['MLAB_MONGO_URI']
# --------------------------------------------------------------------------------

# Zookeeper
zookeeper = os.environ['MLAB_ZOOKEEPER_URI']
# --------------------------------------------------------------------------------

# Flask
flask_prefix = "dashboard"
flask_uri_prefix = "/" + flask_prefix

# Override your secret key
SECRET_KEY = '***REMOVED***'

# Flask-Security config
SECURITY_URL_PREFIX = flask_uri_prefix
SECURITY_PASSWORD_HASH = "***REMOVED***"
SECURITY_PASSWORD_SALT = "***REMOVED***"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/users/"

SECURITY_POST_LOGIN_VIEW = flask_uri_prefix + "/"
SECURITY_POST_LOGOUT_VIEW = flask_uri_prefix + "/"

from application.repositories.mongo_repository import get_concat_mongo_uri

mongo_uri_with_database = get_concat_mongo_uri(mongo_database, mongo_connection_uri)

# db value only mean the project name... it doesn't make sense for me.
MONGODB_SETTINGS = {
    'db': mongo_database,
    'host': mongo_uri_with_database
}
