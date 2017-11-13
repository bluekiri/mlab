# coding: utf-8
from dashboard_server.domain.entities.auth.api_token_model import Token


def is_valid_token(token):
    try:
        t = Token.objects(token=token)
        if not t:
            return False
        return True
    except ValueError:
        return False
