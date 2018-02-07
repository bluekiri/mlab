import logging

from flask_admin.base import AdminViewMeta
from flask_security.core import current_user

from dashboard.application.exceptions.role_listener_not_found_exception import \
    RoleListenerNotFoundException


def generate_meta_roles_calls(cls):
    for role in current_user.roles:
        try:
            call = "cls.has_%s_role()" % role.name
            exec(call)
        except Exception:
            role_exception = RoleListenerNotFoundException()
            role_exception.role = role.name
            raise role_exception


# Crazy run view wrapper
def _run_view(cls, fn, *args, **kwargs):
    try:
        generate_meta_roles_calls(cls)
    except RoleListenerNotFoundException as exception:
        logging.warning(
            "Hey... maybe you forgot to create the listeners for the role %s" % exception.role)

    return fn(cls, *args, **kwargs)


class ViewSecurityListeners(AdminViewMeta):
    def __new__(cls, name, bases, attrs):
        attrs['_run_view'] = _run_view
        return super(ViewSecurityListeners, cls).__new__(cls, name, bases, attrs)
