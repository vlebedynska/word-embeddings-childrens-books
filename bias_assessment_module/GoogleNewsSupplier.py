import os
from shutil import copyfile

from gensim.models import KeyedVectors

from bias_assessment_module.ModelSupplier import ModelSupplier


class GoogleNewsSupplier(ModelSupplier):

    def __init__(self, corpus_path, corpus_config, model_config):
        self._corpus_path = corpus_path
        self._corpus_config = corpus_config
        self._model_config = model_config

    def load_models(self):
        return [self._load_model(self._config_to_id())]

    def _load_model(self, model_id):
        return KeyedVectors.load_word2vec_format(model_id, binary=True)

    def save_models(self):
        copyfile(self._corpus_path + os.path.sep + self._model_config["corpus_name"], self._config_to_id())

    def _save_model(self, model_id, model):
        pass #TODO

    def _config_to_id(self):
        return "{model_path}{corpus_name}".format(**self._model_config)

