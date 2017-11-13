import os

# LDAP
# ldap_server = "***REMOVED***"
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

MONGODB_SETTINGS = {'host': mongo_connection_uri,
                    'db': mongo_database,
                    'port': 27017}
