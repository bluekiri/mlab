# -*- coding: utf-8 -*-
from benchmark.application.controllers.monitor_controller import MonitorController
from benchmark.domain.repositories.model_repository import ModelRepository
from falcon import API


def register_routes(falcon_api: API, model_repository: ModelRepository):
    falcon_api.add_route('/api/hc', MonitorController())
    falcon_api.add_route('/api/benchmark_model',
                         DummyModelController(model_repository=model_repository))
