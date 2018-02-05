# -*- coding: utf-8 -*-

class MonitorController:
    def on_get(self, req, resp):
        resp.media = {"Message": "OK!"}
