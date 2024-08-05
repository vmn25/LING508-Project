import abc
from model.enums import *
from model.generators import *


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def noun_retriever(self, eng_noun) -> Noun:
        raise NotImplementedError

    @abc.abstractmethod
    def store_noun(self, noun) -> Noun:
        raise NotImplementedError

    @abc.abstractmethod
    def remove_noun(self, eng_noun: str) -> Noun:
        raise NotImplementedError
