import datetime
from itertools import groupby

import timeago

from dashboard_server.models.ml_model import MlModel
from dashboard_server.models.worker_mo import Worker


def get_clusters():
    workers = Worker.objects().order_by('host_name')
    clusters = []
    for key, group in groupby(workers, lambda worker: worker.host_name):
        group = [item for item in group]
        clusters.append(
            {"name": key, "swagger_uri": "http://" + str(list(group)[0].host) + ":9090/v1/ui",
             "worker": len(list(group)),
             "ts": timeago.format(max([item.ts for item in group]), datetime.datetime.utcnow()),
             "model_name": list(group)[0].model.name})
    return clusters


def load_model_on_host(host, model_id):
    model_to_load = MlModel.objects(pk=model_id).first()
    Worker.objects(host_name=host).update(set__model=model_to_load, upsert=True)
