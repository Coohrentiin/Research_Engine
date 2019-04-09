import re
import string
import os
import glob
import json
import math
from text import *

class index:
    
    def __init__(self):
        """
        Init an index
        """
        a = open("output/index.json", "w")
        a.close()
        self.path = os.getcwd() + "/output/"
        self.index = {}
        self.size = 0
        self.correspondances = {}
        self.corpus = []
        self.size_corpus=0

    def load_files(self, path):
        """
        path is a folder
        """
        self.corpus = [[name, 0] for name in glob.glob(path)]
        self.size_corpus=len(self.corpus)
        print("Loading a corpus of " + str(self.size_corpus) + " files")
        i = 0
        while i < self.size_corpus:
            self.add_file(self.corpus[i][0], i)
            i = i + 1
            if i / 100 % 100 == 0:
                print(str(int(float(i)/self.size_corpus))+"%")
        self.size = len(self.index)
        self.TFIDF()
        self.save_dict("index", self.index)
        self.save_dict("correspondances", self.corpus)

    def load_index(self, index_path):
        pass
        return 1

    def add_file(self, file_path, text_id):
        """
        Add a specified file to the index
        """
        list_words = text_transformation(file_path, "", "")
        temp_dict = get_occurency(list_words.traited_text)
        for word in temp_dict:
            if word not in self.index.keys():
                self.add_word(word)
            self.update_occurence(word, text_id, temp_dict[word])
    
    def add_word(self, word):
        self.index[word] = []

    def update_occurence(self, word, text_id, occurence):
        for occ in self.index[word]:
            if text_id == occ[0]:
                occ[1] = occurence
                return 1
        self.index[word].append([text_id, occurence])

    def save_dict(self, name, element):
        name=self.path + name + ".json"
        with open(name, 'w') as json_file:
            json.dump(element, json_file)

    def download(self, name, element):
        name=self.path+name+'.json'
        with open(name) as json_file:
            data = json.load(json_file)
        return(data)
    
    def TFIDF(self):
        for word in self.index:
            i = 0
            while i < len(self.index[word]):
                self.index[word][i][1] = self.index[word][i][1] * math.log(self.size_corpus/len(self.index[word]))
                self.corpus[self.index[word][i][0]][1] += self.index[word][i][1] * self.index[word][i][1]
                i += 1
        for document in self.corpus:
            document[1] = document[1]**(0.5)


        