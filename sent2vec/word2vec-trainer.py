#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html


"""

"""

import logging
import sys
import os
from word2vec import Word2Vec, Sent2Vec, LineSentence


lang='en'

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))
input_dir = '/Share/local/a.aghasadeghi/phrase2vector/Data/wiki/'
input_file='wiki.tok.'+lang+'.tmp'
model = Word2Vec(LineSentence(input_dir+input_file), size=200, window=5, sg=0, min_count=5, workers=20)
model.save(input_dir+'models/'+input_file + '.model')
model.save_word2vec_format(input_dir+'models/'+input_file + '.word.vec')


