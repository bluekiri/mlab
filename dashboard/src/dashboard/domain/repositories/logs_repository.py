# coding: utf-8
from typing import List

from dashboard.domain.entities.logs import Logs


class LogsRepository:
    def get_all_logs(self) -> List[Logs]:
        raise NotImplementedError()

    def get_logs_by_topics(self, topic: List[str]) -> List[Logs]:
        raise NotImplementedError()

    def save(self, log: Logs):
        raise NotImplementedError()
