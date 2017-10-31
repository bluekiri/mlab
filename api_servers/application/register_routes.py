# -*- coding: utf-8 -*-
from falcon import API

from api_servers.application.controllers.monitor_controller import MonitorController


def register_routes(falcon_api: API):
    falcon_api.add_route('/api/hc', MonitorController())
