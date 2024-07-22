from model.generators import *


def test_noun_constructor():
    noun = Noun("dog", "con", "chó")
    assert noun.eng == "dog"
    assert noun.classifier == "con"
    assert noun.viet == "chó"


def test_noun_string():
    noun = Noun("dog", "con", "chó")
    assert noun.result() == "Input: dog \nOutput: con chó"


def test_pronoun_constructor():
    pro = Pronoun("anh", "masculine", "second-person", "singular", "older brother age")
    assert pro.surface_form == "anh"
    assert pro.gender == "masculine"
    assert pro.person == "second-person"
    assert pro.number == "singular"
    assert pro.relationship == "older brother age"


def test_pronoun_result():
    pro = Pronoun("anh", "masculine", "second-person", "singular", "older brother age")
    assert pro.result() == "Input: anh \nOutput: masculine, second-person, singular, older brother age"
