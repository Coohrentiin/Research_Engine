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
            result = self.add_file_to_index(self.corpus[i][0], i) # add the document to the corpus
            if result == 0:
                i = i + 1
            if i / 100 % 100 == 0:
                print(str(int(float(i)/self.size_corpus))+"%")
        self.size = len(self.index) # save 
        self.Update_TFIDF_Index() # transform the occurences to TFIDF value using the current index
        self.save_dict("index", self.index) #save index in output folder in .jason
        self.save_dict("corpus", self.corpus) #save corpus (correspondance table) in output folder in .jason

    def load_index(self, index_path, corpus_path):
        """
        Load a existing index as the current index and current corpus of the class
        """
        temp = self.download_previous(index_path)
        if temp != None:
            self.path = index_path
            self.index = temp
            self.size = len(self.index)
            temp = self.download_previous(corpus_path)
            if temp != None:
                self.corpus = self.download_previous(corpus_path)
                self.size_corpus = len(self.corpus)
                return 0
        return -1

    def add_file_to_index(self, file_path, text_id):
        """
        Add a specified file to the index
        """
        try:
            a = open(file_path, "r")
        except FileNotFoundError:
            print("Error" + file_path + "not found")
            return -1
        text = a.read()
        a.close()
        list_words = clean_text(text)
        temp_dict = get_occurency(list_words)
        for word in temp_dict: #update keys, and words in the index
            if word not in self.index.keys():
                self.add_word(word)
            self.update_occurence(word, text_id, temp_dict[word])
        return 0
    
    def add_word(self, word):
        """
        Add a word in the index
        """
        self.index[word] = []

    def update_occurence(self, word, text_id, occurence):
        """
        Update or the occurence of a word in a text in the index
        """
        for occ in self.index[word]:
            if text_id == occ[0]: #if the index already has a value for word in this text
                occ[1] = occurence
                return 1
        self.index[word].append([text_id, occurence])

    def save_dict(self, name, element):
        """
        save as json file the element under name.json
        """
        name=self.path + name + ".json"
        with open(name, 'w') as json_file:
            json.dump(element, json_file)

    def download_previous(self, path):
        """
        load a json file as a python element (depending on what is loaded)
        """
        try:
            temp = open(path, "r")
            temp.close()
        except FileNotFoundError:
            return None
        with open(path) as json_file:
            data = json.load(json_file)
        return(data)

    def get_indexed_word(self, word):
        """
        get the list associated with the indexed word. Empty list if the word doesn't exist
        """
        if word in self.index:
            return self.index[word]
        temp = []
        return temp
    
    def get_corpus(self):
        """
        get the corpus of the index
        """
        return self.corpus

    def Update_TFIDF_Index(self):
        """
        transform the occurences to TFIDF value using the current index
        """
        for word in self.index:
            i = 0
            while i < len(self.index[word]):
                self.index[word][i][1] = self.TFIDF(word, self.index[word][i][1])
                self.corpus[self.index[word][i][0]][1] += self.index[word][i][1] * self.index[word][i][1]
                i += 1
        for document in self.corpus:
            document[1] = document[1]**(0.5)

    
    def TFIDF(self, word, frequence):
        """
        compute from the frequence of the word in its text and the weight of the text in the corpus the TFIDF of a word
        """
        if word in self.index:
            return frequence * math.log(self.size_corpus/len(self.index[word]))
        return 0


        