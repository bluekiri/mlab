from ldap3 import Server, Connection, ALL_ATTRIBUTES, SIMPLE

from dashboard.application.conf.config import *


def get_user_by_username_info(username):
    server = Server(LDAP_SERVER_URI)
    conn = Connection(server, ldap_dn, ldap_pwd, auto_bind=True, version=3, authentication=SIMPLE, receive_timeout=1)
    filter_account_name = '(|(%s=%s)(%s=%s))' % ("sAMAccountName", username, "mail", username)
    conn.search(ldap_base, filter_account_name, attributes=ALL_ATTRIBUTES)
    return None if not len(conn.entries) else conn.entries[0]


def is_correct_pwd(username, pwd):
    user_entry = get_user_by_username_info(username)
    if user_entry is None:
        return False
    server = Server(LDAP_SERVER_URI)
    conn = Connection(server, str(user_entry.distinguishedName), pwd, version=3, authentication=SIMPLE,
                      receive_timeout=1)
    return conn.bind()
