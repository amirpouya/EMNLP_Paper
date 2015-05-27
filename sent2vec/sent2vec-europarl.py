import logging
import sys
import os
from word2vec import Word2Vec, Sent2Vec, LineSentence

lang='es'
base_url='/NFS/Common/Sent2Vec/Data/wiki/models/'



logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))
input_file = base_url+lang+'/wiki.'+lang




#sent_file='/Share/local/a.aghasadeghi/phrase2vector/Europarl_vec_exp/phrases/uniq.es'
sent_file='t4v.es'
model = Sent2Vec(LineSentence(sent_file), model_file=input_file+'.model')
model.save_sent2vec_format(sent_file + '.vec')
