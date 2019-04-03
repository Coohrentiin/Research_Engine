import glob
import time
<<<<<<< HEAD
#from text import replace_split
#from text import split_function
from text import text_transformation
=======
from text import *
>>>>>>> fc64d15f478a3e3b771ea527c972e459772d8112


# Function used to compare the speed of different method to clean the data
def compare_speed():
    corpus = glob.glob("../../SearchEngineProject2/guardian/00/*")
    end1 = 0
    end2 = 0
    end3 = 0
    for i in corpus:
        a = open(i, "r")
        new = a.read()
        start1 = time.time()
        replace_split(new)
        end1 = time.time() - start1 + end1
        start2 = time.time()
        # split_function(new)
        end2 = time.time() - start2 + end2
        start3 = time.time()
        #nltk_function(new)
        end3 = time.time() - start3 + end3
    return end1, end2, end3
    

# Decomment here what you want to test
#print(compare_speed())

text1=text_transformation('__SXSWi__Secrets_of_the_news_aggregators.txt','/../..','/SearchEngineProject2/guardian/00')
print(text1.traited_text)
