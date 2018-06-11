# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

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
