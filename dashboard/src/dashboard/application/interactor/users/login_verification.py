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

from dashboard.application.repositories.ldap_repository import \
    get_user_by_username_info, \
    is_correct_pwd
from dashboard.domain.entities.auth.login_model import User


class LoginVerification:
    def __init__(self, security_repository):
        pass

    def is_success_pwd(self, username, pwd):
        return is_correct_pwd(username=username, pwd=pwd)

    def get_user_from_username(self, username):

        if len(users):
            return users

        # Get user from ldap
        user_entry = get_user_by_username_info(username=username)
        if user_entry is not None:
            return User(name=str(user_entry.name),
                        username=str(user_entry.mail).split('@')[0],
                        email=str(user_entry.mail))
