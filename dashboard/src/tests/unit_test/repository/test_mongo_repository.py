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


from unittest import TestCase

from dashboard.application.repositories.mongo_repository import \
    get_concat_mongo_uri


class TestMongoRepository(TestCase):

    def test_get_concat_mongo_uri_receive_only_beginning_part(self):
        mongo_uri = "mongodb://localhost:27017"
        database_name = "test_database"
        self.assertEqual(get_concat_mongo_uri(database_name, mongo_uri),
                         "mongodb://localhost:27017/test_database")

    def test_get_concat_mongo_uri_receive_only_beginning_part2(self):
        mongo_uri = "mongodb://localhost:27017/"
        database_name = "test_database"
        self.assertEqual(get_concat_mongo_uri(database_name, mongo_uri),
                         "mongodb://localhost:27017/test_database")

    def test_get_concat_mongo_uri_receive_full_uri(self):
        mongo_uri = "mongodb://localhost:27017/?readPreference=primary"
        database_name = "test_database"
        self.assertEqual(get_concat_mongo_uri(database_name, mongo_uri),
                         "mongodb://localhost:27017/test_database?readPreference=primary")
