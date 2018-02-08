# -*- coding: utf-8 -*-
from falcon import API

from worker.application.controllers.monitor_controller import MonitorController
from worker.application.controllers.dummy_model_controller import DummyModelController
from worker.domain.repositories.model_repository import ModelRepository


def register_routes(falcon_api: API, model_repository: ModelRepository):
    falcon_api.add_route('/api/hc', MonitorController())
    falcon_api.add_route('/api/mlmodel', DummyModelController(model_repository=model_repository))
