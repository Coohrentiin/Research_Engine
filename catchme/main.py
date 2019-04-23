import os
current_path=os.getcwd()
# path= current_path +"/src"
# os.chdir(path)
from src.index import *
from src.query import *
#os.chdir(current_path)
from pathlib import Path
config_index = Path('output/index.json')
config_corpus = Path('output/corpus.json')

index=index()
if config_corpus.is_file() & config_index.is_file():
    answer=input("A previous corpus is already seved. Do you want to use it? Y/N: ")
    if answer=="Y":
        #dowload the previous index and corpus
        index.load_index(current_path+"/output/index.json", current_path+"/output/corpus.json")
    else:
        answer=input("Do you want to use the corpus in the input folder (Y)? Or another (N)? ")
        if answer=="Y":
            #dowload input corpus
            index.load_files("input/*")
        else:
            path=input("Please give use the path of the corpus to use.\nExample : input/*: ")
            #dowload corpus by his path
            index.load_files(path)
else:
    answer=input("There where already no previous corpus treated. Do you want to use the corpus in the input folder (Y)? Or another (N)? ")
    if answer=="Y":
        #dowload input corpus
        index.load_files("input/*")
    else:
        path=input("Please give use the path of the corpus to use: ")
        #dowload corpus by his path
        index.load_files(path)
# at this point we have index.index ready to use
request=input("lets start? Please give us a request. Enter (N) to stop: ")
while request != "N":
    result = HandleQuery(request,index)
    print("Results in order of pertinence")
    if len(result) == 0:
        print("{ensemble vide}")
    for r in result:
        print(index.corpus[r][0])
    request=input("lets start? Please give us a request. Enter (N) to stop: ")
print("See you later aligator")