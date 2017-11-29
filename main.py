from kazoo.client import KazooClient
from kazoo.client import KeeperState
from kazoo.protocol.states import KazooState

zk = KazooClient("172.18.0.2:2181")


@zk.add_listener
def watch_for_ro(state):
    if state == KazooState.CONNECTED:
        print("Connected")
        if zk.client_state == KeeperState.CONNECTED_RO:
            print("Read only mode!")
        else:
            print("Read/Write mode!")

zk.start()
print("Finish")
zk.randomize_hosts()