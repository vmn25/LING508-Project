from abc import ABC

from db.repository import *
import mysql.connector
from model.generators import *


class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {'user': 'root',
                  'password': 'root',
                  'host': 'localhost',
                  'port': '32000',
                  'database': 'viet'
                  }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        try:
            self.connection.close()
        except:
            pass

    def noun_mapper(self, entry: dict) -> Noun:
        viet_classifier_switcher = {'con': Classifier.CON,
                                    u'quyển': Classifier.QUYEN,
                                    u'cái': Classifier.CAI}
        viet_noun = Noun(entry['eng'], viet_classifier_switcher[entry['classifier']], entry['viet'])
        return viet_noun

    def noun_retriever(self, eng_noun):
        sql = 'SELECT * FROM noun WHERE eng = "' + f"{eng_noun}" + '";'
        self.cursor.execute(sql)
        entry = [{'eng': eng, 'classifier': classifier, 'viet': viet} for (id, eng, classifier, viet) in self.cursor]
        result = self.noun_mapper(entry[0])
        return result
