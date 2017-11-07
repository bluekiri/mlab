import datetime
from itertools import groupby

import timeago

from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.entities.worker_mo import Worker
from dashboard_server.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor


class OrchestationInteractorImp(OrchestationInteractor):
    def get_clusters(self):
        workers = Worker.objects().order_by('host_name')
        clusters = []
        for key, group in groupby(workers, lambda worker: worker.host_name):
            group = [item for item in group]
            model_name = list(group)[0].model.name if list(group)[
                                                          0].model is not None else "No Model loaded"
            clusters.append(
                {"name": key, "swagger_uri": "http://" + str(list(group)[0].host),
                 "worker": len(list(group)),
                 "ts": timeago.format(max([item.ts for item in group]), datetime.datetime.utcnow()),
                 "model_name": model_name})
        return clusters

    def load_model_on_host(self, host, model_id):
        model_to_load = MlModel.objects(pk=model_id).first()
        Worker.objects(host_name=host).update(set__model=model_to_load, upsert=True)
