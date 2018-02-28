# coding: utf-8


class Worker(object):
    def __init__(self, host_name, host, model, number_of_instances, group, up, ts, model_error: bool,
                 model_loaded: bool):
        self.number_of_instances = number_of_instances
        self.model = model
        self.host = host
        self.host_name = host_name
        self.group = group
        self.up = up
        self.ts = ts
        self.model_error = model_error
        self.model_loaded = model_loaded
