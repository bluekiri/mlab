# -*- coding: utf-8 -*-
from application.controllers.benchmark_model_controller import BenchmarkModelController
from application.controllers.monitor_controller import MonitorController
from domain.repositories.model_repository import ModelRepository
from falcon import API


def register_routes(falcon_api: API, model_repository: ModelRepository):
    falcon_api.add_route('/api/hc', MonitorController())
    falcon_api.add_route('/api/benchmark_model',
                         BenchmarkModelController(model_repository=model_repository))
