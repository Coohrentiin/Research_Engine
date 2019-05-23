# -*- coding: utf-8 -*-
#!/usr/local/bin/python3.4

"""
Test Index
"""
import os,sys,inspect
import unittest
import os
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
srcdir = currentdir + "/src"
print(srcdir)
sys.path.insert(0,srcdir) 
from index import *
from query import *
import time
from matplotlib import pyplot as plt

def test_speed():
    ind=index()
    path="SearchEngineProject2/guardian/00/*"
    #path="input/*"
    state = 0
    ind.corpus = [[name, 0] for name in glob.glob(path)] # complete the corpus with the file found in the folder
    global_corpus=ind.corpus
    ind.size_corpus=len(ind.corpus) # save the size of the corpus
    if len(ind.corpus) == 0:
        print("No text files found at " + path)
        return -1
    print("Loading a corpus of " + str(ind.size_corpus) + " files")
    number_of_file=[]
    number_of_word=[]
    time_axis=[];
    local_corpus=[]
    start=time.time()
    for i in range(len(global_corpus)):
        local_corpus.append(global_corpus[i])
        ind.corpus=local_corpus
        state=load_particulary_files(ind)
        if state==-1:
            return(-1)
        time_axis.append(time.time()-start)
        number_of_file.append(len(local_corpus))
        number_of_word.append(len(ind.index))
    plt.ylabel('time (s)')
    plt.xlabel('number of document loaded')
    plt.plot(number_of_file,time_axis,"r")
    print(number_of_file)
    plt.show()
    plt.ylabel('time (s)')
    plt.xlabel('number of words in index')
    plt.plot(number_of_word,time_axis,"b")    
    plt.show()
    return 0

def load_particulary_files(ind):
    file_path=ind.corpus[-1][0]
    text_id=len(ind.corpus)-1
    try:
        a = open(file_path, "r")
        text = a.read()
    except:
        print("Error: " + file_path + " not found or not *.txt")
        return -1
    a.close()
    list_words = clean_text(text)
    temp_dict = get_occurency(list_words)
    for word in temp_dict: #update keys, and words in the index
        if word not in ind.index.keys():
            ind.add_word(word)
        ind.update_occurence(word, text_id, temp_dict[word])
    return 0


class KnownValues(unittest.TestCase):

    def testInitIndex(self):
        """An index should be created when instanced"""
        print("Check if an index can be initiated")
        ind = index()
        self.assertEqual(type(index()), type(ind))
    
    def testLoadIndex(self):
        """An index and corpus should be loaded from existing file"""
        print("Check if an index can be loaded")
        # Create fake index
        false_index = {"what":[0, 2], "is":[0, 2], "banana":[0, 2]}
        false_corpus = ["file.txt", 120]
        with open("temp.json", "w") as json_file:
            json.dump(false_index, json_file)
        with open("temp2.json", "w") as json_file:
            json.dump(false_corpus, json_file)
        ind = index()
        ind.load_index("temp.json", "temp2.json")
        os.remove("temp.json")
        os.remove("temp2.json")
        self.assertEqual(ind.index, false_index)
    
    def testCreateIndex(self):
        """An index and corpus should be created from text"""
        print("Check if an index can be created from text files")
        text1 = "Banana banana banana or banana night ?"
        a = open("temp.txt", "w")
        a.write(text1)
        a.close()
        text2 = "Apple apple apple or apple night ?"
        a = open("temp2.txt", "w")
        a.write(text2)
        a.close()
        ind = index()
        ind.load_files("temp*.txt")
        index_result = {'banana': [[0, 2.772588722239781]], 'night': [[0, 0.0], [1, 0.0]], 'appl': [[1, 2.772588722239781]]}
        self.assertEqual(ind.index, index_result)
    
    def testGetIndexedWord(self):
        """Check if an indexed word can be found in index"""
        print("Check if an indexed word can be found in index")
        ind = index()
        ind.index = {"what":[0, 12], "is":[1,13], "banana":[0,12]}
        self.assertEqual(ind.get_indexed_word("what"), [0,12])
        self.assertEqual(ind.get_indexed_word("is"), [1,13])
        self.assertEqual(ind.get_indexed_word("apple"), [])
    
    def testComplexityIndex(self):
        ind = index()
        ind.load_files("/home/caribou/Documents/ENSTA/1A/in104/IN104_CAPORAL_Clement_SOUBEIRAN_Corentin/SearchEngineProject2/guardian/00/*")
        
if __name__ == "__main__":
    #unittest.main()
    test_speed()



