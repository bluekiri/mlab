# coding: utf-8


class Worker(object):
    def __init__(self, host_name, host, model, number_of_instances, group, up, ts):
        self.number_of_instances = number_of_instances
        self.model = model
        self.host = host
        self.host_name = host_name
        self.group = group
        self.up = up
        self.ts = ts
