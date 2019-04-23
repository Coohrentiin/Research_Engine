import re
import string
import os
import glob
from src.text import *
import src.index

def test_index_creation():
    ind = index.index()
    ind.load_files(os.getcwd()[:-3] + "input/*")
    print(os.getcwd()[:-3] + "input/*")
    print(str(ind.size) + " words have been loaded from a corpus of " + str(len(ind.corpus)) + " files")

def test_index_loader():
    ind = index.index()
    ind.load_index("output/index.json", "../output/correspondances.json")
test_index_creation()