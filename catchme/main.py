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
    answer=input("A previous corpus is already saved. Do you want to use it? Y/N: ")
    if answer=="Y":
        #dowload the previous index and corpus
        state=(index.load_index(current_path+"/output/index.json", current_path+"/output/corpus.json"),1)
    else:
        answer=input("Do you want to use the corpus in the input folder (Y)? Or another (N)? ")
        if answer=="Y":
            #dowload input corpus
            state=(index.load_files("input/*"),2)
        else:
            path=input("Please give use the path of the corpus to use.\nExample : input/*: ")
            #dowload corpus by his path
            state=(index.load_files(path),3)
else:
    answer=input("There where already no previous corpus treated. Do you want to use the corpus in the input folder (Y)? Or another (N)? ")
    if answer=="Y":
        #dowload input corpus
        state=(index.load_files("input/*"),2)
    else:
        path=input("Please give use the path of the corpus to use: ")
        #dowload corpus by his path
        state=(index.load_files(path),3)
# at this point we have index.index ready to use
if state[0]==-1:
    print("Error:")
    if state[1]==1:
        print("in loading index: index unreadable. Please download a corpus to create a new index")
    elif state[1]==2:
        print("in loading files: problems encountered during the processing of the texts mentioned above. Please don't manipulate input file during processing, or indicate the path of the corpus.")
    elif state[1]==3:
        print("in loading files: problems encountered during the processing of the texts mentioned above. Please don't manipulate files during processing, you can also use input folder or give the path of another folder.")
else:
    request=input("lets start? Please give us a request. Enter (N) to stop: ")
    while request != "N":
        result = HandleQuery(request,index)
        print("Results in order of pertinence")
        if result==-1:
            print("Error: during the processing the manipulation of the index for request traetment. Index doens't match with corpus. Please download again corpus")
        elif len(result) == 0:
            print("{empty: No document for this answer}")
        else:
            for r in result:
                print(index.corpus[r][0])
        request=input("lets start? Please give us a request. Enter (N) to stop: ")
    print("See you later aligator")