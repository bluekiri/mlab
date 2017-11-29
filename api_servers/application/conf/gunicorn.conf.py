from api_servers.application.datasource.zk_datasource_imp import ZKDatasourceImp
from api_servers.application.repositories.worker_repository_imp import WorkerRepositoryImp

timeout = 90
graceful_timeout = 60
keepalive = 2

zk_datasource = ZKDatasourceImp()
worker_repository = WorkerRepositoryImp(zk_datasource)


def on_starting(server):
    worker_repository.save_worker(server.cfg.workers)


def _remove_worker_pid(pid):
    # workers = Worker.objects(name=pid, host_name=socket.gethostname())
    # for worker in workers:
    #     worker.delete()
    pass


def worker_abort(worker):
    _remove_worker_pid(str(worker.ppid))


def worker_exit(server, worker):
    _remove_worker_pid(str(worker.ppid))


def child_exit(server, worker):
    _remove_worker_pid(str(worker.ppid))
