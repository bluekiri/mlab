# coding: utf-8
from domain.entities.auth.api_token_model import Token
from domain.interactor.users.token_verification import TokenVerification


class TokenVerificationImp(TokenVerification):
    def is_valid_token(self, token_id: str) -> bool:
        try:
            t = Token.objects(token=token_id)
            if not t:
                return False
        except ValueError:
            return False
        return True
