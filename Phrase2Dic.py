__author__ = 'amir'

pharase_table=open('../Phrase_Table/phrase-table.0-0.1.1').readlines()
en=open('../Vectors/phrase-table/uniq.en.vec').readlines()
es=open('../Vectors/phrase-table/uniq.es.vec').readlines()
out=open('../Vectors/phrase-table.vec','w')
en_dic={}
print 'Reading Files End'

for i,line in enumerate(en):

    try:
        toks=line.split("#s")
        enw=toks[0]
        toks=toks[1].split(' ')
        numb=toks[0].split('_')[1]
        en_dic[enw]=int(numb)
    except:
        pass

es_dic={}
for i,line in enumerate(es):
    try:
        toks=line.split("#s")
        esw=toks[0]
        toks=toks[1].split(' ')
        numb=toks[0].split('_')[1]
        es_dic[esw]=int(numb)
    except:
        pass

print 'Search Starts'
for line in pharase_table:
    try:
        toks=line.strip().split('|')
        toks[0]='sent_'+str(es_dic[toks[0].strip()]);
        toks[1]='sent_'+str(en_dic[toks[1].strip()]);
        print "|".join(toks)
        out.write(" ".join([toks[0],toks[1]])+"\n")
    except:
        print line
