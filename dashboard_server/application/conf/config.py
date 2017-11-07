# LDAP
import os

ldap_server = "***REMOVED***"
ldap_base = "***REMOVED***"
ldap_dn = "***REMOVED***"
ldap_pwd = "***REMOVED***"
ldap_edit_groups = ['***REMOVED***']
ldap_groups = ['g20 - Desarrollo Hotel', 'g15 - Contenidos', '***REMOVED***']
# --------------------------------------------------------------------------------

# Google
google_client_id = "374258396879-a44bf217umr569jdp12gitbqt089shkp.apps.googleusercontent.com"
g_suit_host = ["logitravelgroup.com", "bluekiri.com"]
# --------------------------------------------------------------------------------

# Mongo
mongo_database = os.environ['DATABASE_NAME']
mongo_connection_uri = os.environ['MLAB_MONGO_URI']
# mongo_database = "mlab"
# mongo_connection_uri = "mongodb://mlab_mongo:27017/mlab?readPreference=primary"

# --------------------------------------------------------------------------------


flask_prefix = "dashboard"
flask_uri_prefix = "/" + flask_prefix

# Flask

# Create dummy secrey key so we can use sessions
SECRET_KEY = '***REMOVED***'

# Flask-Security config
SECURITY_URL_PREFIX = flask_uri_prefix
SECURITY_PASSWORD_HASH = "***REMOVED***"
SECURITY_PASSWORD_SALT = "***REMOVED***"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"

SECURITY_POST_LOGIN_VIEW = flask_uri_prefix + "/"
SECURITY_POST_LOGOUT_VIEW = flask_uri_prefix + "/"

MONGODB_SETTINGS = {'host': mongo_connection_uri,
                    'db': mongo_database,
                    'port': 27017}
# --------------------------------------------------------------------------------
