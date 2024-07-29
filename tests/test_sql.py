from db.mysql_repository import *

repo = MysqlRepository()

noun_entry = {'eng': 'dog', 'classifier': 'con', 'viet': u'chó'}


def test_noun_mapper():
    noun_test = repo.noun_mapper(noun_entry)
    assert type(noun_test) == Noun
    assert noun_test.eng == 'dog'
    assert noun_test.classifier == Classifier.CON
    assert noun_test.viet == u'chó'


def test_noun_retrieval():
    eng_noun = 'cat'
    noun_retrieval_test = repo.noun_retriever(eng_noun)
    assert type(noun_retrieval_test) == Noun
    assert noun_retrieval_test.eng == 'cat'
    assert noun_retrieval_test.classifier == Classifier.CON
    assert noun_retrieval_test.viet == u'mèo'