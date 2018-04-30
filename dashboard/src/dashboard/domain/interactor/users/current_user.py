# coding: utf-8

class CurrentUser:
    def get_current_user(self):
        raise NotImplementedError()

    def has_admin_role(self) -> bool:
        raise NotImplementedError()
