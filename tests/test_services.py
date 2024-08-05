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
