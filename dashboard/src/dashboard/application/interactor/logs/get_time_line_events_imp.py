# coding: utf-8
from dashboard.domain.entities.logs import LogsTopics
from dashboard.domain.repositories.logs_repository import LogsRepository
from dashboard.domain.interactor.logs.get_time_line_events import GetTimeLineEvents


class GetTimeLineEventsImp(GetTimeLineEvents):

    def __init__(self, logs_repository: LogsRepository):
        self.logs_repository = logs_repository

    def get_all_time_events(self):
        return self.logs_repository.get_logs_by_topics([LogsTopics.new_model.name])
