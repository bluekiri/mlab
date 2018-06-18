# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Bluekiri V5 BigData Team <bigdata@bluekiri.com>.
#
# This program is free software: you can redistribute it and/or  modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# As a special exception, the copyright holders give permission to link the
# code of portions of this program with the OpenSSL library under certain
# conditions as described in each individual source file and distribute
# linked combinations including the program with the OpenSSL library. You
# must comply with the GNU Affero General Public License in all respects for
# all of the code used other than as permitted herein. If you modify file(s)
# with this exception, you may extend this exception to your version of the
# file(s), but you are not obligated to do so. If you do not wish to do so,
# delete this exception statement from your version. If you delete this
# exception statement from all source files in the program, then also delete
# it in the license file.

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
        return super(ViewSecurityListeners, cls).__new__(cls, name, bases,
                                                         attrs)
