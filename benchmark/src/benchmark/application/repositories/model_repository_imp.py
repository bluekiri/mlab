# -*- coding:utf-8 -*-
from benchmark.domain.entities.model_mo import Model
from benchmark.domain.repositories.model_repository import ModelRepository


class ModelRepositoryImp(ModelRepository):
    def get_model_from_id(self, model_id: str):
        model_query = Model.objects(pk=model_id)
        try:
            return model_query[0].name
        except Exception:
            return None