# coding: utf-8

class OrchestationInteractor:
    def get_clusters(self):
        raise NotImplementedError()

    def load_model_on_host(self, host: str, model_id: str):
        raise NotImplementedError()

    def get_groups(self):
        raise NotImplementedError()

    def set_group_to_cluster(self, host_cluster: str, group_name:str):
        raise NotImplementedError()
