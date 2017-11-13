import datetime
from itertools import groupby

import timeago

from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.entities.worker_mo import Worker
from dashboard_server.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor


class OrchestationInteractorImp(OrchestationInteractor):
    def set_group_to_cluster(self, host_cluster: str, group_name: str):
        Worker.objects(host_name=host_cluster).update(set__group=group_name, upsert=True)

    def _get_workers_grouped(self):
        workers = Worker.objects().order_by('host_name')
        clusters = []
        for key, host_group in groupby(workers, lambda worker: worker.host_name):
            host_group = [item for item in host_group]
            model_name = list(host_group)[0].model.name if list(host_group)[
                                                               0].model is not None else "No Model loaded"
            clusters.append(
                {"name": key, "swagger_uri": "http://" + str(list(host_group)[0].host),
                 "worker": len(list(host_group)),
                 "ts": timeago.format(max([item.ts for item in host_group]),
                                      datetime.datetime.utcnow()),
                 "model_name": model_name,
                 "group": str(list(host_group)[0].group)})
        return clusters

    def get_clusters(self):
        groups = {}

        clusters = self._get_workers_grouped()
        for cluster in clusters:
            if cluster["group"] in groups.keys():
                groups[cluster["group"]].append(cluster)
            else:
                groups[cluster["group"]] = [cluster]
        return groups

    def load_model_on_host(self, host, model_id):
        model_to_load = MlModel.objects(pk=model_id).first()
        Worker.objects(host_name=host).update(set__model=model_to_load, upsert=True)

    def get_groups(self):
        workers = Worker.objects()
        return list(set([worker.group for worker in workers if worker.group is not None]))
