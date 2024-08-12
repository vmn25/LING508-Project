import db.mysql_repository
from model.generators import *
import re
from translate import Translator

class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def change_repo(self, repo):
        self.repo = repo

    #Use case 2: Takes English noun and returns Viet translation with appropriate classifier if applicable
    def noun_classifier(self, noun) -> Noun:
        if self.repo.noun_retriever(noun):
            return self.repo.noun_retriever(noun)
        else:
            translator = Translator(to_lang="vi")
            translated = translator.translate('the '+noun)
            translated = re.sub(r'[^\w\s]', '', translated)
            translated_lower = translated.lower()
            translated_split = translated_lower.split()
            result = Noun(noun, translated_split[0], " ".join(translated_split[1:]))
            self.repo.store_noun(result)
            return result

    def add_noun(self, noun):
        if self.repo.noun_retriever(noun.eng):
            return False
        else:
            self.repo.store_noun(noun)
            return True

    def parse_noun(self, data):
        stored_noun = data.get('noun')
        res = Noun(stored_noun.get('english'), stored_noun.get('classifier'), stored_noun.get('vietnamese'))
        return res
