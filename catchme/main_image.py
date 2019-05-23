# -*- coding: utf-8 -*-
#!/usr/local/bin/python3.4


# !#! WARNINGS !#!
# note that for this code you need to double check
# the path to the right folder.

import os,sys,inspect
from pathlib import Path
config_index = Path('output/index_image.json')
config_corpus = Path('output/corpus_image.json')
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
srcdir = currentdir + "/src"
sys.path.insert(0,srcdir)
from index import *
from query import *
from text import *
imgdir = currentdir + "/SearchEngineProject2/clustering"
sys.path.insert(0,imgdir)
from create_clusters import *
from request import *

# Create index
ind=index()
folder_name = 'SearchEngineProject2/clustering/image_dataset_descriptors/'
saving_path = 'SearchEngineProject2/clustering/saved_kmeans'
result = dataset_handling(folder_name, saving_path)
ind.load_images(result)

# Create request
name_dataset_file = 'SearchEngineProject2/clustering/image_dataset_descriptors/dataset_imagesall_souls.json'
image_name = 'all_souls_000091'

req = request_handling(folder_name, saving_path, name_dataset_file, image_name)
result = list(HandleImageQuery(req,ind))
result.reverse()

# print result in order
for r in result:
    print(ind.corpus[r][0])