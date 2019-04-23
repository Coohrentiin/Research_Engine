import os
current_path=os.getcwd()
path= current_path +"/src"
os.chdir(path)
from index import *

os.chdir(os.chdir(path))
index_exists = os.path.isfile('/output/index.json')
corpus_exists = os.path.isfile('/output/corpus.json')
index=index()
if index_exists & corpus_exists:
    answer=input("A previous corpus is already seved. Do you want to use it? Y/N")
    if answer=="Y":
        #dowload the previous index and corpus
    else:
        answer=input("Do you want to use the corpus in the input folder (Y)? Or another (N)?")
        if answer=="Y":
            #dowload input corpus
            index.load_files(index.path)
        else:
            path=input("Please give use the path of the corpus to use:")
            #dowload corpus by is path
            index.load_files(path)
else:
    answer=input("There where already no previous corpus treated. Do you want to use the corpus in the input folder (Y)? Or another (N)?")
    if answer=="Y":
        #dowload input corpus
        index.load_files(index.path)
    else:
        path=input("Please give use the path of the corpus to use:")
        #dowload corpus by is path
        index.load_files(path)