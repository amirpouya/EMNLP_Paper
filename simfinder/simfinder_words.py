__author__ = 'amir'
import numpy as np
import fileReader
import time
dic_file_addr='../../Vectors/words/lex.f2e'
dic_file_r_addr='../../Vectors/words/lex.e2f'
Direct_TM_file_addr='../../TM/w.es2en.tm'
Inverce_TM_file_addr='../../TM/w.en2es.tm'
source_vec_addr='../../models/es/wiki.tok.es.cbow'
target_vec_addr='../../models/en/wiki.tok.en.cbow'

out_dr_addr='../../Vectors/words/new-lex.f2e'
out_in_addr='../../Vectors/words/new-lex.e2f'

out_dr_addr='new-lex.f2e'
out_in_addr='new-lex.e2f'


out=open(out_dr_addr,'w')
out2=open(out_in_addr,'w')

print 'Reading input File'
dic_file=open(dic_file_addr).readlines()
print 'Reading Revece input File'
dic_file_r=open(dic_file_r_addr).readlines()
print 'Reading TM File Direct'
r_tm=np.matrix(np.loadtxt(Direct_TM_file_addr))
print 'Reading TM File Inverse'
d_tm=np.matrix(np.loadtxt(Inverce_TM_file_addr))
print 'Reading Source File'
source_vecs=open(source_vec_addr).readlines()
source_vecs=fileReader.fileRead(source_vecs,' ')
print 'Reading Target File'
target_vecs=open(target_vec_addr).readlines()
target_vecs=fileReader.fileRead(target_vecs,' ')

error_counter=0
print 'Source 2 Target'
for i,line in enumerate(dic_file):
    try:
        #print line
        tic=time.time()
        toks=line.split( )
        try:
            #print tok[0],tok[1]
            trg_vec=fileReader.normalize(np.matrix(np.fromstring(target_vecs[toks[0]],float,sep=' ')))
            src_vec=fileReader.normalize(np.matrix(np.fromstring(source_vecs[toks[1]],float,sep=' ')))
            src_vec2=src_vec*d_tm
            score=-trg_vec*src_vec2.T
            score=score.item(0)
        except KeyError:
            score=float(toks[2])
            error_counter+=1
            continue
        out.write(toks[0]+' '+toks[1]+' '+str(round(score,7))+'\n')
        #print time.time()-tic
    except KeyError:
        pass
        print 'error error',toks[0],toks[1]
print 'Source 2 Target:',error_counter
print 'Target 2 Source'
error_counter=0
for i,line in enumerate(dic_file_r):
    try:
        #print line
        tic=time.time()
        toks=line.split( )
        try:
            #print tok[0],tok[1]
            trg_vec=fileReader.normalize(np.matrix(np.fromstring(target_vecs[toks[1]],float,sep=' ')))
            src_vec=fileReader.normalize(np.matrix(np.fromstring(source_vecs[toks[0]],float,sep=' ')))
            trg_vec2=trg_vec*r_tm
            score=-src_vec*trg_vec2.T
            score=score.item(0)
        except KeyError:
            score=float(toks[2])
            error_counter+=1
            continue
        out2.write(toks[0]+' '+toks[1]+' '+str(round(score,7))+'\n')
        #print time.time()-tic
    except KeyError:
        pass
        print 'error error',toks[0],toks[1]
print 'Target 2 Source:',error_counter

