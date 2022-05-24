import numpy as np
import nltk
import os
import ahocorasick
import pyecharts

class Entity_Extractor:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])

        self.city_path = os.path.join(cur_dir, 'data/city.txt')

        self.city_wds = [i.strip() for i in open(self.city_path) if i.strip()]

        self.region_tree = self.build_actree(list(self.city_wds))

    '''构造actree，加速过滤'''
    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    '''问句过滤'''
    def check_medical(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            print(i)

    '''构造词对应的类型'''
    def build_wdtype_dict(self):
        wd_dict = dict()

        return wd_dict

question = Entity_Extractor()
print(question.check_medical("where is Paris"))


