from index import *
import operator

def HandleQuery(request,index):
    #request segmentation in words
    correspondances=clem_process()
    doc_list={}
    request_seg=clean_text(request)
    request_occurency=get_occurency(request_seg)
    result_list=[]
    euclidian_query_sum=0
    for word in request_seg:
        freq=request_occurency[word]
        data_about_word= get_indexed_word(word) #function_of_a_word like: [[doc_number,w_i_f],[doc_number,w_i_f],[doc_number,w_i_f]]
        n=len(data_about_word)
        weight=index.TFIDF(word,freq)
        for i in range(n): #for each doc where the word appear:
            doc=data_about_word[i][0]
            if doc in doc_list:
                doc_list[doc]+=data_about_word[i][0]*weight
            else:
                doc_list[doc]=data_about_word[i][0]*weight
        euclidian_query_sum+=weight**2
    euclidian_query_sum=euclidian_query_sum**0.5
    for doc in doc_list:
        doc_list[doc]=doc_list[doc]/(correspondances[doc]*euclidian_query_sum)
    sorted_list=sorted(doc_list.items(), key=operator.itemgetter(1),reverse=True)
    return(zip(*sorted_list)[0])
    