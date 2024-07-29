import abc
from model.enums import *
from model.generators import *


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def noun_retriever(self, eng_noun) -> Noun:
        raise NotImplementedError
