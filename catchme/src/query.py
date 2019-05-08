from src.index import *
import operator

def HandleQuery(request,index):
    """
    Fonction that return the ordered list of text based on the similarities with the request and the index
    request is a sentence, index is an oject of index class
    """
    correspondances=index.corpus
    doc_list={} #dictionary
    request_seg=clean_text(request) #treatment of the request to create a list of word treated as the corpus (lemmatization, tokenization)
    request_occurency=get_occurency(request_seg) #get_occurency is a function of text.py imported in index.py. It return a dictionnary with occurency of each words for each word of the list. We check if it's in the dictonary if not, we add it and update its occurency else we update its occurency
    result_list=[] #list of
    euclidian_query_sum=0
    for word in request_seg: #for each treated word of the request
        freq=request_occurency[word] 
        data_about_word= index.get_indexed_word(word) #function_of_a_word like: [[doc_number,w_i_f],[doc_number,w_i_f],[doc_number,w_i_f]]
        n=len(data_about_word)
        weight=index.TFIDF(word,freq) #classic TFIDF weight of the word in the request
        for i in range(n): #for each doc where the word appear:
            doc=data_about_word[i][0]
            if doc in doc_list:
                doc_list[doc]+=data_about_word[i][0]*weight #weigh of the word in the document weighted by the classic TFIDF weight of the word in the request
            else:
                doc_list[doc]=data_about_word[i][0]*weight
        euclidian_query_sum+=weight**2
    euclidian_query_sum=euclidian_query_sum**0.5 #total euclidien sum of the query 
    for doc in doc_list:
        if doc in correspondances:
            doc_list[doc]=doc_list[doc]/(correspondances[doc][1]*euclidian_query_sum) #calculation of the value of the comparison number between documents
        else:
            return -1
    sorted_list=sorted(doc_list.items(), key=operator.itemgetter(1),reverse=True)
    temp=list(zip(*sorted_list))
    if len(temp) > 0:
        return(temp[0]) #we return the list of ducument were request word appear sorted from most relevant to least relevant (with the value of the comparison number)
    return []
    