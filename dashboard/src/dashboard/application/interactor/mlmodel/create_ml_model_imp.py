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
