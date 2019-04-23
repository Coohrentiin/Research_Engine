import os
# current_path=os.getcwd()
# path= current_path +"/src"
# os.chdir(path)
from src.index import *
from src.query import *
#os.chdir(current_path)

index_exists = os.path.isfile('/src/output/index.json')
corpus_exists = os.path.isfile('/src/output/corpus.json')
index=index()
if index_exists & corpus_exists:
    answer=input("A previous corpus is already seved. Do you want to use it? Y/N")
    if answer=="Y":
        #dowload the previous index and corpus
        index.load_files("input/*")
    else:
        answer=input("Do you want to use the corpus in the input folder (Y)? Or another (N)?")
        if answer=="Y":
            #dowload input corpus
            index.load_files(index.path)
        else:
            path=input("Please give use the path of the corpus to use:")
            #dowload corpus by his path
            index.load_files(path)
else:
    answer=input("There where already no previous corpus treated. Do you want to use the corpus in the input folder (Y)? Or another (N)?")
    if answer=="Y":
        #dowload input corpus
        index.load_files("input/*")
    else:
        path=input("Please give use the path of the corpus to use:")
        #dowload corpus by his path
        index.load_files(path)
# at this point we have index.index ready to use
request=input("lets start? Please give us a request:")
result = HandleQuery(request,index)
print("Results in order of pertinence")
if len(result) == 0:
    print("")
for r in result:
    print(index.corpus[r][0])
index.save_dict("index", index.index)
index.save_dict("corpus", index.corpus)