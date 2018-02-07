from mongoengine import Q

from dashboard.application.repositories.ldap_repository import get_user_by_username_info, \
    is_correct_pwd
from dashboard.domain.entities.auth.login_model import User


# def is_valid_username(username):
#     user_entry = get_user_by_username_info(username=username)
#     return user_entry is not None
#
#
# def has_edit_permission(username):
#     user_entry = get_user_by_username_info(username=username)
#     if user_entry is not None:
#         return any(edit_group in user_group for user_group in user_entry.memberOf for edit_group in
#                    ldap_edit_groups)


def is_success_pwd(username, pwd):
    return is_correct_pwd(username=username, pwd=pwd)


def update_last_entry(user):
    pass


def get_user_from_username(username):
    # Get user from mongo
    users = list(User.objects(Q(email=username) | Q(username=str(username).split('@')[0])))
    if len(users):
        return users[0]

    # Get user from ldap
    user_entry = get_user_by_username_info(username=username)
    if user_entry is not None:
        return User(name=str(user_entry.name), username=str(user_entry.mail).split('@')[0],
                    email=str(user_entry.mail))
