# coding: utf-8
from dashboard_server.domain.interactor.users.users_privilages import UsersPrivilages


class UsersPrivilagesImp(UsersPrivilages):
    def can_change_models(self, username: str) -> bool:
        # user = User.objects(username=username)
        # TODO
        return True
