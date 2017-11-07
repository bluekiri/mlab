# coding: utf-8

class OrchestationInteractor:
    def get_clusters(self):
        raise NotImplementedError()

    def load_model_on_host(self, host: str, model_id: str):
        raise NotImplementedError()
