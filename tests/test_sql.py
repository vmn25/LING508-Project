from db.mysql_repository import *

repo = MysqlRepository()

def test_noun_retrieval():
    eng_noun = 'cat'
    noun_retrieval_test = repo.noun_retriever(eng_noun)
    assert type(noun_retrieval_test) == Noun
    assert noun_retrieval_test.eng == 'cat'
    assert noun_retrieval_test.classifier == Classifier.CON
    assert noun_retrieval_test.viet == u'mèo'