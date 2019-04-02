# Class that create a clean data set with all the words from a document
# It processes Tokenisation, Stop words and Lemmatization
# IN :
#   path : path of the document from which the clean data will be generated
# OUT :
#   words : list of string containing the words from the given document

import re 
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string
# class TextProcessing:
#     __init__(self,):
#         file=open(,"r")

def nltk_function(text_string):
    stopWords = list(stopwords.words('english')) + list(string.punctuation)
    words = word_tokenize(text_string)
    wordsFiltered = []
    
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    
    return wordsFiltered

def replace_split(text_string):
    return re.sub("[^a-zA-Z \']+", '', text_string).split()

def split_function(text_string):
    text_in_list=[]
    i=0
    while i <len(text_string):
        if text_string[i]==' ' or text_string[i]=='.' or text_string[i]=='!' or text_string[i]==':' or text_string[i]==',' or text_string[i]=='?' or text_string[i]==';' or text_string[i]=='!' or text_string[i]=='(' or text_string[i]==')':
            text_in_list.append(text_string[:i])
            text_string=text_string[i+1:]
            i=0
        elif text_string[i:i+1]=="\n":
            text_in_list.append(text_string[:i])
            text_string=text_string[i+2:]
            i=0
        elif text_string[i]=="'":
            text_string=text_string[:i]+" "+text_string[i+1:]
            i=i+1
        elif text_string[i]=='"':
            text_string=text_string[:i]+text_string[i+1:]
        else:
            i=i+1
    return(text_in_list)

def tokenisation(a_word):
    n=len(a_word)
    list_word=[]
    if n>=3:
        if a_word[n-3:n]=="n t":
            list_word.append(a_word[:n-3])
            list_word.append("not")
            return(list_word)
        if a_word[n-2:n]==" s":
             list_word.append(a_word[:n-2])
             return(list_word)  
    list_word.append(a_word)
    return list_word

stop_word_english = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}

def stop_words(a_word):
    if a_word in stop_word_english:
        return(True)
    return(False)

def irregular_vb_list():
    ir_vb = []
    crimefile = open("irregularverbs.irv", 'r')
    for line in crimefile.readlines():
        ir_vb.append([line])
        for i in line.split(","):
          ir_vb[-1].append(i)

def lemmatization(a_word):
    return(True)
