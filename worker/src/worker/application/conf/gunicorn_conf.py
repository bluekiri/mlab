import time

from worker.application.datasource.zk_datasource_imp import ZKDatasourceImp
from worker.application.repositories.worker_repository_imp import WorkerRepositoryImp

timeout = 90
graceful_timeout = 60
keepalive = 2

zk_datasource = ZKDatasourceImp()
worker_repository = WorkerRepositoryImp(zk_datasource)


def on_starting(server):
    max_tries = 15
    tries = 0
    while worker_repository.is_current_worker_loaded_on_zoo() and tries < max_tries:
        time.sleep(1)
        tries += 1
        if tries == max_tries:
            raise TimeoutError()

    worker_repository.save_worker(server.cfg.workers)
