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
