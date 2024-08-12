from abc import ABC

from db.repository import *
import mysql.connector
from model.generators import *


class MysqlRepository(Repository):
    noun_sql = ("INSERT INTO noun "
                "(eng, classifier, viet) "
                "VALUES (%(eng)s, %(classifier)s, %(viet)s)")

    remove_noun_sql = ("DELETE FROM noun "
                       "WHERE eng = %(eng)s")
    def __init__(self):
        super().__init__()
        config = {'user': 'root',
                  'password': 'root',
                  'host': 'db',  # to run locally, 'localhost'
                  'port': '3306',  # to run locally, '32000'
                  'database': 'viet'
                  }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        try:
            self.connection.close()
        except:
            pass

    def noun_retriever(self, eng_noun):
        sql = 'SELECT * FROM noun WHERE eng = "' + f"{eng_noun}" + '" LIMIT 1;'
        self.cursor.execute(sql)
        rows = list(self.cursor.fetchall())
        if not self.cursor.rowcount:
            return None
        nouns = [Noun(eng, classifier, viet) for (id, eng, classifier, viet) in rows]
        return nouns[0]

    def store_noun(self, noun):
        data_noun = {
            'eng': noun.eng,
            'classifier': noun.classifier.value,
            'viet': noun.viet,
        }
        self.cursor.execute(self.noun_sql, data_noun)
        self.connection.commit()

    def remove_noun(self, eng_noun: str):
        data_noun = {'eng': eng_noun}
        self.cursor.execute(self.remove_noun_sql, data_noun)
        self.connection.commit()
