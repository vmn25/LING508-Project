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

    def result(self):
        return ("Input: " + self.surface_form +
                " \nOutput: " + self.gender +
                ", " + self.person + ", " +
                self.number + ", " + self.relationship)


class Noun(Word):
    def __init__(self, eng: str, classifier: str, viet: str):
        super().__init__(eng, PartOfSpeech.NOUN)
        self.eng = eng
        self.classifier = classifier
        self.viet = viet

    def result(self):
        return "Input: " + self.eng + " \nOutput: " + self.classifier + " " + self.viet
