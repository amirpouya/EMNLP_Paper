__author__ = 'amir'

pharase_table=open('phrase-table.0-0.1.1')
en=open('../Vectors/phrase-table/uniq.en.vec').readlines()
es=open('../Vectors/phrase-table/uniq.es.vec').readlines()
out=open('../Vectors/phrase-table.vec','w')


out_en_vec=open('../Vectors/phrase.vec.en','w')
out_es_vec=open('../Vectors/phrase.vec.es','w')

out_en_dic=open('../Vectors/phrase.dic.en','w')
out_es_dic=open('../Vectors/phrase.dic.es','w')


en_dic={}
es_dic={}
out_en_vec.write('200  200\n')
out_es_vec.write('200 200\n')
print 'Start Reading EN'
for i,line in enumerate(en):
    try:
        toks=line.split("#s")
        enw=toks[0]
        toks=toks[1].split(' ')

        numb=toks[0].split('_')[1]
        en_dic[enw.strip()]=numb
        out_en_vec.write('sent_'+numb+' '+' '.join(toks[1:]))
        out_en_dic.write('sent_'+numb+'|'+enw.strip()+'\n')
    except IndexError:
        pass
en=''
print 'Start Reading ES'
for i,line in enumerate(es):
    try:
        toks=line.split("#s")
        esw=toks[0]
        toks=toks[1].split(' ')
        numb=toks[0].split('_')[1]
        es_dic[esw.strip()]=numb
        out_es_vec.write('sent_'+numb+' '+' '.join(toks[1:]))
        out_es_dic.write('sent_'+numb+'|'+esw.strip()+'\n')
    except IndexError:
        pass
es=''
#exit()
print 'Start Search...'
with open('../Phrase_Table/phrase-table.0-0.1.1') as pharase_table:
    for line in pharase_table:
        try:

            toks=line.strip().split('|')
            if toks[0].strip()=='! &quot;':
                print toks
                #exit()
            toks[0]='sent_'+str(es_dic[toks[0].strip()]);

            toks[1]='sent_'+str(en_dic[toks[1].strip()]);
            #print "|".join(toks)
            out.write(" ".join([toks[0],toks[1]])+"\n")
        except :
            print line

