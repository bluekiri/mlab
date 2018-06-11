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

import os

PROJECT_SUFFIX = "-mlab"
PROJECT = "Demo" + PROJECT_SUFFIX
SERVICE_PORT = os.environ['PORT']

# Mongodb
MONGO_DATABASE = os.environ['DATABASE_NAME']
MONGO_CONNECTION_URI = os.environ['MLAB_MONGO_URI']

# Zookeeper
ZOOKEEPER = os.environ['MLAB_ZOOKEEPER_URI']

# Mail
SERVER_MAIL = os.environ.get("MLAB_MAIL_SERVER", "")
SERVER_FROM_USER = os.environ.get("NO_REPLY_USER", "")
SERVER_FROM_PASSWORD = os.environ.get("NO_REPLY_PASS", "")
