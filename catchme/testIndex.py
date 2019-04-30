"""
Test Index
"""

import src.index
from src.query import *
import unittest
import os

class KnownValues(unittest.TestCase):

    def testInitIndex(self):
        """An index should be created when instanced"""
        print("Check if an index can be initiated")
        index = src.index.index()
        self.assertEqual(type(src.index.index()), type(index))
    
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
        index = src.index.index()
        index.load_index("temp.json", "temp2.json")
        os.remove("temp.json")
        os.remove("temp2.json")
        self.assertEqual(index.index, false_index)
    
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
        index = src.index.index()
        index.load_files("temp*.txt")
        index_result = {'banana': [[0, 2.772588722239781]], 'night': [[0, 0.0], [1, 0.0]], 'appl': [[1, 2.772588722239781]]}
        self.assertEqual(index.index, index_result)
    
    def testGetIndexedWord(self):
        """Check if an indexed word can be found in index"""
        print("Check if an indexed word can be found in index")
        index = src.index.index()
        index.index = {"what":[0, 12], "is":[1,13], "banana":[0,12]}
        self.assertEqual(index.get_indexed_word("what"), [0,12])
        self.assertEqual(index.get_indexed_word("is"), [1,13])
        self.assertEqual(index.get_indexed_word("apple"), [])

if __name__ == "__main__":
    unittest.main()
