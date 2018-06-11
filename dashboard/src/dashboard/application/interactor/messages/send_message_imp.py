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

from dashboard.domain.entities.message import Message, Topic, SubjectData
from dashboard.domain.entities.ml_model import MlModel
from dashboard.domain.interactor.messages.send_message import SendMessage
from dashboard.domain.repositories.messages_repository import MessageRepository


class SendMessageImp(SendMessage):
    def __init__(self, messages_repository: MessageRepository):
        self.messages_repository = messages_repository

    def new_model_message(self, model: MlModel):
        message = Message()
        message.topic = Topic.new_model.name
        message.subject_data = SubjectData.new_model.name
        message.subject = SubjectData.new_model.value['text']
        message.text = "Model name %s" % model.name
        self.messages_repository.save_message(message)
