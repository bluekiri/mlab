# coding: utf-8
from domain.interactor.users.users_privileges import UsersPrivileges


class UsersPrivilegesImp(UsersPrivileges):
    def can_change_models(self, username: str) -> bool:
        # user = User.objects(username=username)
        # TODO
        return True
