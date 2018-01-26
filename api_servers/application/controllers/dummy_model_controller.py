# coding: utf-8
from application.controllers.base_model_controller import BaseModelController


class DummyModelController(BaseModelController):
    def on_get(self, req, resp):
        model_wrapper = self.model_repository.get_current_model()
        if model_wrapper is not None:
            model = model_wrapper.get_model_instance()
        else:
            raise Exception("Model not found...")

        model_request = {}
        resp.media = {"model_response": model.run_model(model_request)}
