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


_mongo_connection = None


def get_mongo_connection():
    global _mongo_connection
    if _mongo_connection is None:
        from flask_mongoengine import MongoEngine
        _mongo_connection = MongoEngine()
    return _mongo_connection


def get_concat_mongo_uri(database, mongo_uri):
    import re
    match = re.match(r'(mongodb:\/\/[a-z:\._\-0-9]+\/?)(.*)', mongo_uri)
    slash_database = '/' + database
    if match is None or len(match.groups()) > 2:
        raise ConnectionError("Invalid mongo uri connection %s" % mongo_uri)
    match_groups = [item for item in match.groups() if
                    item is not None and len(item) > 0]
    if len(match_groups) == 2:
        return database.join(match_groups)
    if mongo_uri[-1] == '/':
        return mongo_uri + database
    return mongo_uri + slash_database
