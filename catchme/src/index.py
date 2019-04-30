import re
import string
import os
import glob
import json
import math
from src.text import *

class index:

    def __init__(self):
        self.path = os.getcwd() + "/output/" # save where the index is saved
        self.index = {} # table with all the words and their TFIDF and in which document they appear
        # for example index = {"hello": [[0, 0.5], [1, 0.2]]}
        self.size = 0 # number of words in the index
        self.corpus = [] # list with the path to the text and its euclidien norm 
        # for example corpus = [["text.txt", 65], ["test3", 0.34]]
        self.size_corpus=0 # number of documents in the corpus

    def load_files(self, path):
        """
        load_files create the index and corpus objects from a corpus located at path
        path is a folder
        Example : input/*
        """
        self.corpus = [[name, 0] for name in glob.glob(path)] # complete the corpus with the file found in the folder
        self.size_corpus=len(self.corpus) # save the size of the corpus

        print("Loading a corpus of " + str(self.size_corpus) + " files")

        # start to load each document in the index
        i = 0
        while i < self.size_corpus: # for each document
            self.add_file_to_index(self.corpus[i][0], i) # add the document to the corpus
            i = i + 1
            if i / 100 % 100 == 0:
                print(str(int(float(i)/self.size_corpus))+"%")
        self.size = len(self.index) # save 
        self.Update_TFIDF_Index()
        self.save_dict("index", self.index)
        self.save_dict("corpus", self.corpus)

    def load_index(self, index_path, corpus_path):
        self.path = index_path
        self.index = self.download_previous(self.path)
        self.size = len(self.index)
        self.corpus = self.download_previous(corpus_path)
        self.size_corpus = len(self.corpus)

    def add_file_to_index(self, file_path, text_id):
        """
        Add a specified file to the index
        """
        a = open(file_path, "r")
        text = a.read()
        a.close()
        list_words = clean_text(text)
        temp_dict = get_occurency(list_words)
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

    def download_previous(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
        return(data)

    def get_indexed_word(self, word):
        if word in self.index:
            return self.index[word]
        temp = []
        return temp
    
    def get_corpus(self):
        return self.corpus

    def Update_TFIDF_Index(self):
        for word in self.index:
            i = 0
            while i < len(self.index[word]):
                self.index[word][i][1] = self.TFIDF(word, self.index[word][i][1])
                self.corpus[self.index[word][i][0]][1] += self.index[word][i][1] * self.index[word][i][1]
                i += 1
        for document in self.corpus:
            document[1] = document[1]**(0.5)

    
    def TFIDF(self, word, frequence):
        if word in self.index:
            return frequence * math.log(self.size_corpus/len(self.index[word]))
        return 0


        