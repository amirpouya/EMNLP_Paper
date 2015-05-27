__author__ = 'amir'
import numpy as np
import fileReader
import time
dic_file_addr='../../Vectors/phrase-table-proc/phrase-table.vec'
Direct_TM_file_addr='../../TM/p.es2en.tm'
Inverce_TM_file_addr='../../TM/p.en2es.tm'
source_vec_addr='../../Vectors/phrase-table-proc/phrase.vec.es'
target_vec_addr='../../Vectors/phrase-table-proc/phrase.vec.en'
en_dic_addr='../../Vectors/phrase-table-proc/phrase.dic.en'
es_dic_addr='../../Vectors/phrase-table-proc/phrase.dic.es'
out_addr='../../Vectors/new-phrasetable'

out=open(out_addr,'w')

print 'Reading input File'
dic_file=open(dic_file_addr).readlines()
print 'Reading TM File Direct'
d_tm=np.matrix(np.loadtxt(Direct_TM_file_addr))
print 'Reading TM File Inverse'
r_tm=np.matrix(np.loadtxt(Inverce_TM_file_addr))
print 'Reading Source File'
source_vec=open(source_vec_addr).readlines()
source_vec=fileReader.fileRead(source_vec,' ')
print 'Reading Target File'
target_vec=open(target_vec_addr).readlines()
target_vec=fileReader.fileRead(target_vec,' ')
print 'Reading EN Dic'
en_dic=open(en_dic_addr).readlines()
en_dic=fileReader.fileRead(en_dic,'|')
print 'Readin ES Dic'
es_dic=open(es_dic_addr).readlines()
es_dic=fileReader.fileRead(es_dic,'|')


for line in dic_file:
    try:
        tic=time.time()
        toks=line.split()
        trg_vec=fileReader.normalize(np.matrix(np.fromstring(target_vec[toks[1]],float,sep=' ')))
        src_vec=fileReader.normalize(np.matrix(np.fromstring(target_vec[toks[0]],float,sep=' ')))
        src_vec2=src_vec*d_tm
        trg_vec2=trg_vec*r_tm
        score=-trg_vec*src_vec2.T
        score2=-src_vec*trg_vec2.T

        out.write(es_dic[toks[0]]+'|||'+en_dic[toks[1]]+'|||'+str(round(score.item(0),7))+" "+str(round(score2.item(0),7))+'\n')
        print time.time()-tic
    except KeyError:
        pass
        print 'error error',toks[0],toks[1]


