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

from datetime import datetime

from dashboard.domain.entities.ml_model import MlModel
from dashboard.domain.interactor.logs.save_model_log_event import \
    SaveModelLogEvent
from dashboard.domain.interactor.messages.send_message import SendMessage
from dashboard.domain.interactor.mlmodel.create_ml_model import CreateMlModel
from dashboard.domain.repositories.model_repository import ModelRepository


class CreateMlModelImp(CreateMlModel):
    def __init__(self, send_message: SendMessage,
                 save_model_log_event: SaveModelLogEvent,
                 model_repository: ModelRepository):
        self.send_message = send_message
        self.save_model_log_event = save_model_log_event
        self.model_repository = model_repository

    def create(self, name: str, score: float, description: str, pickle,
               creator_id: str,
               images=None):
        model = MlModel(name=name, description=description,
                        ts=datetime.utcnow(),
                        pickle=pickle, score=score)
        self.model_repository.save(model)
        self.save_model_log_event.save_new_model_event(model_id=str(model.pk),
                                                       model_name=model.name,
                                                       is_system_event=False,
                                                       source_id=creator_id)
        self.send_message.new_model_message(model)
        return model.pk
