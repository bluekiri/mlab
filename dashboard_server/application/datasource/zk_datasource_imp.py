# coding: utf-8
from kazoo.client import KazooClient

from application.conf.config import zookeeper


class ZKDatasourceImp:
    def __init__(self):
        self.zk = KazooClient(zookeeper)
        self.zk.start()

    def update_or_create(self, path, node, data):
        if self.zk.exists("%s/%s" % (path, node)) is not None:
            self.zk.set("%s/%s" % (path, node), data.encode("utf-8"))
        else:
            self.zk.create("%s/%s" % (path, node),data.encode("utf-8"))