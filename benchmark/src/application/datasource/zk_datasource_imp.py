# coding: utf-8
from kazoo.client import KazooClient

from api_server.application.conf.config import ZOOKEEPER


class ZKDatasourceImp:
    def __init__(self):
        self.zk = KazooClient(ZOOKEEPER)
        self.zk.start()
