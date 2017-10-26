from oauth2client import client, crypt

from dashboard_server.conf.config import google_client_id, g_suit_host


def is_sig_in_outh_token_verificated(token):
    try:
        idinfo = client.verify_id_token(token, google_client_id)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")

            # If auth request is from a G Suite domain:
        if not any(idinfo['hd'] == host for host in g_suit_host):
            raise crypt.AppIdentityError("Wrong hosted domain.")
        return True
    except crypt.AppIdentityError:
        return False
        # userid = idinfo['sub']


def get_mail_from_token(token):
    idinfo = client.verify_id_token(token, google_client_id)
    return idinfo['email']
