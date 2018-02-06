# coding: utf-8

from unittest import TestCase

from application.repositories.mongo_repository import get_concat_mongo_uri


class TestMongoRepository(TestCase):

    def test_get_concat_mongo_uri_receive_only_beginning_part(self):
        mongo_uri = "mongodb://localhost:27017"
        database_name = "test_database"
        self.assertEqual(get_concat_mongo_uri(database_name, mongo_uri), "mongodb://localhost:27017/test_database")

    def test_get_concat_mongo_uri_receive_only_beginning_part2(self):
        mongo_uri = "mongodb://localhost:27017/"
        database_name = "test_database"
        self.assertEqual(get_concat_mongo_uri(database_name, mongo_uri), "mongodb://localhost:27017/test_database")

    def test_get_concat_mongo_uri_receive_full_uri(self):
        mongo_uri = "mongodb://localhost:27017/?readPreference=primary"
        database_name = "test_database"
        self.assertEqual(get_concat_mongo_uri(database_name, mongo_uri),
                         "mongodb://localhost:27017/test_database?readPreference=primary")
