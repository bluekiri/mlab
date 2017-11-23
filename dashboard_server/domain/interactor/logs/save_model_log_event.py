# coding:utf-8
from typing import List


class SaveModelLogEvent:
    def save_new_model_event(self, model_name: str, model_id: str, is_system_event: bool,source_id:str):
        raise NotImplementedError()

    def save_activate_model_event(self, model_name: str, model_id: str, host: List[str],
                                  is_system_event: bool, source_id: str):
        raise NotImplementedError()

    def save_activate_model_by_group_event(self, model_name: str, model_id: str, host: List[str],
                                           group_name: str, is_system_event: bool,source_id:str):
        raise NotImplementedError()
