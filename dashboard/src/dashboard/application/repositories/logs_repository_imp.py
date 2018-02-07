# coding: utf-8
import datetime
from typing import List

from dashboard.domain.entities.logs import Logs
from dashboard.domain.repositories.logs_repository import LogsRepository


class LogsRepositoryImp(LogsRepository):
    def get_all_logs(self) -> List[Logs]:
        return list(Logs.objects())

    def get_logs_by_topics(self, topic: List[str]) -> List[Logs]:
        return list(Logs.objects(topic__in=topic))

    def save(self, log: Logs):
        log.ts = datetime.datetime.utcnow()
        log.save()
