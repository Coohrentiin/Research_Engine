# Class that create a clean data set with all the words from a document
# It processes Tokenisation, Stop words and Lemmatization
# IN :
#   path : path of the document from which the clean data will be generated
# OUT :
#   words : list of string containing the words from the given document

import re
import string
import os

from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 


''' 
from nltk.corpus import stopwordsapt-
from nltk.tokenize import sent_tokenize, word_tokenize

# class TextProcessing:
#     __init__(self,):
#         file=open(,"r")

def nltk_function(self.All_text):
    stopWords = list(stopwords.words('english')) + list(string.punctuation)
    words = word_tokenize(self.All_text)
    wordsFiltered = []
    
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    
    return wordsFiltered

print(nltk_function("Bonjour je suis, un lapin\n gna/."))
'''

def replace_split(text):
    return re.sub("[^a-zA-Z \']+", '', text).split()

stop_word_english = {'','ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}


class text_transformation:
    """
    text1=text_transformation("text1.txt","../../SearchEnginProject2/")
    text1.traited_text
    is a list of the text1 words 

    we must code others functions in this class to create the index
    """
    def __init__(self,name,path_from_here1,path_from_here2):
        """
        exemple:
        name='__SXSWi__Secrets_of_the_news_aggregators.txt'
        path1='/../..'
        path2='/SearchEngineProject2/00'

        """
        self.current_path=os.getcwd()
        path_of_file=os.getcwd()+path_from_here1
        os.chdir(path_of_file)
        path_of_file=os.getcwd()+path_from_here2
        os.chdir(path_of_file)
        self.file=open(name)
        self.All_text=self.file.read()
        self.file.close()
        os.chdir(self.current_path)
        self.text_split=self.split_function()
        self.traited_text=[]
        self.irregular_vb_list()
        for a_word in self.text_split:
            list_a_word=self.tokenisation(a_word)
            for a_piece_of_a_word in list_a_word:
                if not self.stop_words(a_piece_of_a_word):
                    self.traited_text.append(self.lemmatization(a_piece_of_a_word))

    def split_function(self):
        text_in_list=[]
        i=0
        while i <len(self.All_text):
            if self.All_text[i]==' ' or self.All_text[i]=='.' or self.All_text[i]=='!' or self.All_text[i]==':' or self.All_text[i]==',' or self.All_text[i]=='?' or self.All_text[i]==';' or self.All_text[i]=='!' or self.All_text[i]=='(' or self.All_text[i]==')':
                text_in_list.append(self.All_text[:i])
                self.All_text=self.All_text[i+1:]
                i=0
            elif self.All_text[i:i+1]=="\n":
                text_in_list.append(self.All_text[:i])
                self.All_text=self.All_text[i+2:]
                i=0
            elif self.All_text[i]=="'":
                self.All_text=self.All_text[:i]+" "+self.All_text[i+1:]
                i=i+1
            elif self.All_text[i]=='"':
                self.All_text=self.All_text[:i]+self.All_text[i+1:]
            else:
                i=i+1
        return(text_in_list)

    def tokenisation(self,a_word):
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

    def stop_words(self,a_word):
        if a_word in stop_word_english:
            return(True)
        return(False)

    def irregular_vb_list(self):
        global ir_vb
        ir_vb = []
        crimefile = open("irregularverbs.txt", 'r')
        for line in crimefile.readlines():
            ir_vb.append(line.split(" ")[:3])
    #        for i in line.split(" "):
    #          ir_vb[-1].append(i)
        global n_ir_vb
        n_ir_vb = len(ir_vb)

    def lemmatization(self,a_word):
        for i in range(n_ir_vb):
            if a_word in ir_vb[i]:
                return(ir_vb[i][0])
        if len(a_word)>2 and a_word[-2:]=="ed":
            return(a_word[:-2])
        if len(a_word)>3 and a_word[-3:]=="ing":
            return(a_word[:-3])
        return(a_word)

def get_occurency(list_word):
    '''
    This function return a dictionnary with occurency of each words
    for each word of the list we check if it's in the dictonary
    if not, we add it and update its occurency
    else we update its occurency
    '''
    dictionnary={}
    for word in list_word:
        if word in dictionnary:
            dictionnary[word]+=1
        else:
            dictionnary[word]=1
    return(dictionnary)


tokenizer = RegexpTokenizer(r'\w+')
ps = PorterStemmer()   
stop_words = set(stopwords.words('english'))
def clean_text(text):
    global tokenizer
    global ps  
    global stop_words
    token_text = tokenizer.tokenize(text)
    lowers = [word.lower() for word in token_text]
    filtered_text = [str(ps.stem(w)) for w in lowers if not w in stop_words]
    return(filtered_text)
    