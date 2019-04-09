import re
import string
import os
import glob
from text import *
import index

def test_index_creation():
    ind = index.index()
    ind.load_files("input/*")
    print(str(ind.size) + " words have been loaded from a corpus of " + str(len(ind.corpus)) + " files")

test_index_creation()