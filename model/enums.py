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
    CON = "con"
    CAI = "cái"
    DOI = "đôi"
    BO = "bộ"
    QUA = "quả"
    CHIEC = "chiếc"
    CAY = "cây"
    MON = "món"
    THOI = "thỏi"
    QUYEN = "quyển"
    LY = "ly"
    TACH = "tách"
    CHEN = "chén"
    CHAI = "chai"
    DIA = "dĩa"
    CUC = "cục"
    SOI = "sợi"
    CHO = "chỗ"
    CUON = "cuộn"
    DIEU = "điếu"
    GOI = "gói"
    CHUYEN = "chuyện"
    BAN = "bản"
    NGOI = "ngôi"
    MIENG = "miếng"
    BONG = "bông"
    LAN = "lần"
    PHONG = "phòng"
    NGUOI = "người"
