# coding: utf-8
from benchmark.domain.interactors.model_validator import ModelValidator


class ModelValidatorImp(ModelValidator):

    def __init__(self, model_respository):
        self.model_respository = model_respository

    def test_model_response(self):
        pass

    def validate(self, model_id: str) -> bool:
        try:
            self.model_respository.get_model_from_id(model_id)

            return True
        except Exception as e:
            return False
