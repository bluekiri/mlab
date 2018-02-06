# coding: utf-8
from kazoo.client import KazooClient

from dashboard_server.application.conf.config import ZOOKEEPER


class ZKDatasourceImp:
    def __init__(self):
        self.zk = KazooClient(ZOOKEEPER)
        self.zk.start()

    def update_or_create(self, path, node, data):
        if self.zk.exists("%s/%s" % (path, node)) is not None:
            self.zk.set("%s/%s" % (path, node), data.encode("utf-8"))
        else:
            self.zk.create("%s/%s" % (path, node),data.encode("utf-8"))
