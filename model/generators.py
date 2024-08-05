from model.enums import *


class Word:
    def __init__(self, surface_form: str, pos: PartOfSpeech):
        self.surface_form = surface_form
        self.pos = pos


class Pronoun(Word):
    def __init__(self, surface_form: str, gender: str, person: str, number: str, relationship: str):
        super().__init__(surface_form, PartOfSpeech.NOUN)
        self.surface_form = surface_form
        self.gender = gender
        self.person = person
        self.number = number
        self.relationship = relationship

    def __str__(self):
        return ("Input: " + self.surface_form +
                " \nOutput: " + self.gender +
                ", " + self.person + ", " +
                self.number + ", " + self.relationship)


class Noun(Word):
    def __init__(self, eng: str, classifier: str, viet: str):
        super().__init__(eng, PartOfSpeech.NOUN)
        self.eng = eng
        self.classifier = self.classifier_mapper(classifier)
        self.viet = viet

    def classifier_mapper(self, classifier: str) -> Classifier:
        viet_classifier_switcher = {'con': Classifier.CON,
                                    u'quyển': Classifier.QUYEN,
                                    u'cái': Classifier.CAI,
                                    u'đôi': Classifier.DOI,
                                    u'bộ': Classifier.BO,
                                    u'quả': Classifier.QUA,
                                    u'chiếc': Classifier.CHIEC,
                                    u'cây': Classifier.CAY,
                                    u'món': Classifier.MON,
                                    u'thỏi': Classifier.THOI,
                                    u'ly': Classifier.LY,
                                    u'tách': Classifier.TACH,
                                    u'chén': Classifier.CHEN,
                                    u'chai': Classifier.CHAI,
                                    u'dĩa': Classifier.DIA,
                                    u'cục': Classifier.CUC,
                                    u'sợi': Classifier.SOI,
                                    u'chỗ': Classifier.CHO,
                                    u'cuộn': Classifier.CUON,
                                    u'điếu': Classifier.DIEU,
                                    u'gói': Classifier.GOI,
                                    u'chuyện': Classifier.CHUYEN,
                                    u'bản': Classifier.BAN,
                                    u'ngôi': Classifier.NGOI,
                                    u'miếng': Classifier.MIENG,
                                    u'bông': Classifier.BONG,
                                    u'lần': Classifier.LAN,
                                    u'phòng': Classifier.PHONG,
                                    }
        return viet_classifier_switcher[classifier]

    def __str__(self):
        return "Input: " + self.eng + " \nOutput: " + self.classifier.value + " " + self.viet