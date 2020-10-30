# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from contextlib import contextmanager
from .expm import *
from ..utils import Wrapper


class QlibRecorder:
    def __init__(self, exp_manager, default_uri, current_uri):
        self.exp_manager = exp_manager
        self.default_uri = default_uri
        self.current_uri = current_uri

    @contextmanager
    def start(self, experiment_name):
        run = self.start_exp(experiment_name, self.current_uri)
        yield run
        self.end_exp()

    def start_exp(self, experiment_name=None):
        return self.exp_manager.start_exp(experiment_name, self.current_uri)

    def end_exp(self):
        self.exp_manager.end_exp()

    def search_records(self, experiment_ids, **kwargs):
        return self.exp_manager.search_records(experiment_ids, **kwargs)

    def get_exp(self, experiment_id=None, experiment_name=None):
        return self.exp_manager.get_exp(experiment_id, experiment_name)

    def delete_exp(self, experiment_id):
        self.exp_manager.delete_exp(experiment_id)

    def get_uri(self, type):
        return self.exp_manager.get_uri(type)

    def get_recorder(self):
        return self.exp_manager.active_recorder

    def save_object(self, data=None, name=None, local_path=None):
        self.exp_manager.active_recorder.save_object(data, name, local_path)

    def save_objects(self, data_name_list=None, local_path=None):
        self.exp_manager.active_recorder.save_objects(data_name_list, local_path)

    def load_object(self, name):
        return self.exp_manager.active_recorder.load_object(name)

    def log_params(self, **kwargs):
        self.exp_manager.active_recorder.log_params(**kwargs)

    def log_metrics(self, step=None, **kwargs):
        self.exp_manager.active_recorder.log_metrics(step, **kwargs)

    def set_tags(self, **kwargs):
        self.exp_manager.active_recorder.set_tags(**kwargs)

    def delete_tag(self, key):
        self.exp_manager.active_recorder.delete_tag(key)


# global record
R = Wrapper()