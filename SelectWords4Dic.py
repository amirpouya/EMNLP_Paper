__author__ = 'amir'

outfile=open('../Vectors/words/selected-dic','w')
dicfile=open('../Vectors/words/es-en.dic').readlines()

es_dic=[(i,item.split()[0]) for i,item in enumerate(dicfile)]
en_dic=[(i,item.split()[1]) for i,item in enumerate(dicfile)]
print 'Reading Dics end'


es_vec=open('../models/es/wiki.tok.es.cbow').readlines()
es_vec=[item.split()[0] for item in es_vec[1:]]
print 'Reading ES models end'

en_vec=open('../models/en/wiki.tok.en.cbow').readlines()
en_vec=[item.split()[0] for item in en_vec[1:]]
print 'Reading EN models end'
counter=0

for i,es_item in enumerate(es_dic):
    if es_item[1] in es_vec and en_dic[es_item[0]][1] in en_vec:
        print es_item[1],en_dic[es_item[0]][1]
        outfile.write(es_item[1]+' '+en_dic[es_item[0]][1]+'\n')
        counter+=1
print counter
