from app.services import *


def test_noun_classifier():
    result = Services().noun_classifier("book")
    assert result.eng == "book"
    assert result.classifier == Classifier.QUYEN
    assert result.viet == "sách"

    result = Services().noun_classifier("cat")
    assert result.eng == "cat"
    assert result.classifier == Classifier.CON
    assert result.viet == "mèo"


def test_noun_not_in_db():
    repo = db.mysql_repository.MysqlRepository()
    service = Services()
    service.change_repo(repo)
    repo.remove_noun("cow")
    assert not repo.noun_retriever("cow")

    result = service.noun_classifier("cow")
    assert result.eng == "cow"
    assert result.classifier == Classifier.CON
    assert result.viet == "bò"


def test_noun_storage():
    repo = db.mysql_repository.MysqlRepository()
    service = Services()
    service.change_repo(repo)
    repo.remove_noun("cow")
    assert not repo.noun_retriever("cow")
    service.noun_classifier("cow")

    retrieved_noun = repo.noun_retriever("cow")
    assert retrieved_noun.eng == "cow"
    assert retrieved_noun.classifier == Classifier.CON
    assert retrieved_noun.viet == "bò"

def test_store_noun():
    repo = db.mysql_repository.MysqlRepository()
    test_noun = Noun("hat", "cái", "nón")
    repo.remove_noun("hat")
    assert not repo.noun_retriever("hat")
    repo.store_noun(test_noun)

    stored_noun = repo.noun_retriever("hat")
    assert stored_noun.eng == "hat"
    assert stored_noun.classifier == Classifier.CAI
    assert stored_noun.viet == "nón"


def test_remove_noun():
    repo = db.mysql_repository.MysqlRepository()
    assert repo.noun_retriever("book")
    repo.remove_noun("book")

    assert not repo.noun_retriever("book")
