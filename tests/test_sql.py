import db
from db.mysql_repository import *

repo = MysqlRepository()


def test_noun_retrieval():
    eng_noun = 'cat'
    noun_retrieval_test = repo.noun_retriever(eng_noun)
    assert type(noun_retrieval_test) == Noun
    assert noun_retrieval_test.eng == 'cat'
    assert noun_retrieval_test.classifier == Classifier.CON
    assert noun_retrieval_test.viet == u'mèo'


def test_store_noun():
    test_noun = Noun("hat", "cái", "nón")
    repo.remove_noun("hat")
    assert not repo.noun_retriever("hat")
    repo.store_noun(test_noun)

    stored_noun = repo.noun_retriever("hat")
    assert stored_noun.eng == "hat"
    assert stored_noun.classifier == Classifier.CAI
    assert stored_noun.viet == "nón"


def test_remove_noun():
    assert repo.noun_retriever("book")
    repo.remove_noun("book")

    assert not repo.noun_retriever("book")
