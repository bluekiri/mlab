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


import smtplib

from worker.application.conf.config import SERVER_MAIL, SERVER_FROM_USER, \
    SERVER_FROM_PASSWORD
from worker.domain.repositories.user_repository import UserRepository
from worker.domain.interactors.send_mail import SendMail


class SendMailImp(SendMail):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def send(self, to, message, subject):
        server = smtplib.SMTP(SERVER_MAIL, 587)
        server.ehlo()
        server.starttls()
        server.login(SERVER_FROM_USER, SERVER_FROM_PASSWORD)
        server.sendmail(SERVER_FROM_USER, to, message)
        server.close()

    def send_to_topic(self, topic, message, subject):
        users = list(self.user_repository.get_users_by_topic(topic))
        for user in users:
            self.send(user.email, message, subject)
