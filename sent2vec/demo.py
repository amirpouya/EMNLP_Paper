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




logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))
input_file = 'paper-datas/datas/paper.en'
'''
model = Word2Vec(LineSentence(input_file), size=200, window=5, sg=0, min_count=5, workers=8)
model.save(input_file + '.model')
model.save_word2vec_format(input_file + '.word.vec')

sent_file= 'paper-datas/datas/paper.en'
model = Sent2Vec(LineSentence(sent_file), model_file=input_file+'.model')
model.save_sent2vec_format(sent_file + '.vec')

'''
sent_file= 'paper-datas/datas/paper.en'
input_file = sent_file
vec_file = sent_file+'.vec'
input_lines=open(input_file).readlines();
vec_lines=open(vec_file).readlines();
output=open('paper-datas/will-use/en/paper.en.vec','w')
output.writelines(vec_lines[0])
for k,line in enumerate(input_lines):
    #print k,line

    toks=line.split('<==')
    temp=toks[0].replace('==>','');
    temp=temp.strip().replace('.txt','')
    print k
    output.writelines(vec_lines[k+1].replace('sent_'+str(k),temp))

