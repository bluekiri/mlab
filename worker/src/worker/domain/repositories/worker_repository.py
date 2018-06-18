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


class WorkerRepository:
    def get_worker_host(self):
        raise NotImplementedError()

    def initialize_event_listener(self):
        raise NotImplementedError()

    def remove_worker_from_host(self, worker_name: str, host_name: str):
        raise NotImplementedError()

    def subscribe_on_worker_model_change(self, callback_function):
        raise NotImplementedError()

    def save_worker(self, number_of_instances: int):
        raise NotImplementedError()

    def get_self_worker_model_id(self) -> str:
        raise NotImplementedError()

    def set_success_model_load(self):
        raise NotImplementedError()

    def set_error_modal_load(self):
        raise NotImplementedError()

    def is_current_worker_loaded_on_zoo(self):
        raise NotImplementedError
