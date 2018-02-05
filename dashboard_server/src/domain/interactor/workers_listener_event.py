# coding: utf-8

class WorkersListenerEvent:
    def on_new_worker(self):
        raise NotImplementedError()

    def on_worker_down(self):
        raise NotImplementedError()

    def on_worker_up(self):
        raise NotImplementedError()
