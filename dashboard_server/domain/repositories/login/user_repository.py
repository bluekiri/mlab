# coding: utf-8
from domain.entities.auth.login_model import User


class UserRepository:
    def is_valid_username(self, username: str) -> bool:
        raise NotImplementedError()

    def has_edit_permission(self, username: str) -> bool:
        raise NotImplementedError()

    def is_success_pwd(self, username: str, pwd: str) -> bool:
        raise NotImplementedError()

    def update_last_entry(self, user: User):
        raise NotImplementedError()

    def get_user_from_username(self, username: str) -> User:
        raise NotImplementedError()
