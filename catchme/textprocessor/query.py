
def query(request,docs):
    #request segmentation in words
    doc_list={}
    request_seg=clean_text(request)
    request_weight={}
    dic={}
    s=0
    for word in request_seg:
        request_weight[word]=tfidf_word(word)
        for doc in docs:
            if doc in doc_list:
                score=
                doc_list{doc}=score
            else:
                doc_list{doc}=score