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

from ldap3 import Server, Connection, ALL_ATTRIBUTES, SIMPLE

from dashboard.application.conf.config import *
from dashboard.domain.repositories.ldap_repository import LdapRepository


class LdapRepositoryImp(LdapRepository):

    def get_user_by_username_info(self, username):
        try:
            server = Server(LDAP_SERVER_URI)
            conn = Connection(server, LDAP_DN, LDAP_PWD, auto_bind=True,
                              version=3,
                              authentication=SIMPLE,
                              receive_timeout=1)
            filter_account_name = '(|(%s=%s)(%s=%s))' % (
                "sAMAccountName", username, "mail", username)
            conn.search(LDAP_BASE, filter_account_name,
                        attributes=ALL_ATTRIBUTES)
            return None if not len(conn.entries) else conn.entries[0]
        except:
            return None

    def is_correct_pwd(self, username, pwd):
        user_entry = self.get_user_by_username_info(username)
        if user_entry is None:
            return False
        server = Server(LDAP_SERVER_URI)
        conn = Connection(server, str(user_entry.distinguishedName), pwd,
                          version=3,
                          authentication=SIMPLE,
                          receive_timeout=1)
        return conn.bind()
