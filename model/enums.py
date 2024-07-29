from enum import Enum


class Gender(Enum):
    UNISEX = 1
    MASCULINE = 2
    FEMININE = 3


class PartOfSpeech(Enum):
    NOUN = 1
    DEMONSTRATIVE_NOUN_MODIFIER = 2
    ARTICLE = 3
    CLASSIFIER = 4
    NUMERAL = 5
    QUANTIFIER = 6
    FOCUS_MARKER_PARTICLE = 7
    VERB = 8
    ADJ = 9
    ADV = 10
    PREP = 11


class Relationship(Enum):
    FAMILIAR = 1
    FORMAL = 2
    DISRESPECTFUL = 3
    OLDER_BROTHER_AGE = 4
    OLDER_SISTER_AGE = 5
    YOUNGER = 6
    OLDER_UNCLE_AUNT_AGE = 7
    YOUNGER_UNCLE_AGE = 8
    YOUNGER_AUNT_AGE = 9
    GRANDFATHER_AGE = 10
    GRANDMOTHER_AGE = 11


class Person(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Number(Enum):
    SINGULAR = 1
    PLURAL = 2


class Classifier(Enum):
    CON = 1
    CAI = 2
    DOI = 3
    BO = 4
    QUA = 5
    CHIEC = 6
    CAY = 7
    MON = 8
    THOI = 9
    QUYEN = 10
    LY = 11
    TACH = 12
    CHEN = 13
    CHAI = 14
    DIA = 15
    CUC = 16
    SOI = 17
    CHO = 18
    CUON = 19
    DIEU = 20
    GOI = 21
    CHUYEN = 22
    BAN = 23
    NGOI = 24
    MIENG = 25
    BONG = 26
    LAN = 27
    PHONG = 28
    NGUOI = 29
