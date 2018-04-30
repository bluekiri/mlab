# coding: utf-8
from flask_login import current_user

from dashboard.domain.interactor.users.current_user import CurrentUser


class CurrentUserImp(CurrentUser):
    def get_current_user(self):
        return current_user

    def has_admin_role(self) -> bool:
        return current_user.has_role("admin")
