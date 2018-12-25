import gensim
from gensim.corpora import WikiCorpus, MmCorpus
from gensim import corpora, models, similarities
from gensim.utils import simple_preprocess
from gensim.models import LsiModel

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text ('./results/results_wordids.txt.bz2')
mm = gensim.corpora.MmCorpus('./results/results_tfidf.mm')
print(mm)
# MmCorpus(93674 documents, 33663 features, 7987319 non-zero entries)

# train LSI model
model_lsi = LsiModel(corpus=mm, id2word=id2word, num_topics=400)
model_lsi.save('./results/lsi.lsi_model')

# index wikicorpus documents
index = similarities.MatrixSimilarity(model_lsi[mm],num_features=400)
index.save('./results/lsi_index.mm')

# test
query = ['Keywords and their placing versus highly defined featured snippets from Google are more important for getting traffic on webpage.', 'How to build up super snippets for new web content?']

sims_list = []
# sims_list: cosine similarity between query and wikicorpus documents.  (index,(doc_id, similarity_value))

for item in query: 
    vec_bow = id2word.doc2bow(gensim.utils.simple_preprocess(item))  # or item.lower().split()
    vec_lsi = model_lsi[vec_bow]
    sims = index[vec_lsi]
    sims_list.append(list(enumerate(sims)))
# print(sims_list[0])
# print(sims_list[1])

# select similarity_value>0
s_1 = list([index for index in sims_list[0] if index[1] > 0])
# print(s_1)
s_2 = list([index for index in sims_list[1] if index[1] > 0])
# print(s_2)

# calculate the similary based document numbers
DS1 = len(s_1)/(len(s_1)+len(s_2))
DS2 = len(s_2)/(len(s_1)+len(s_2))
print(DS1, DS2)
