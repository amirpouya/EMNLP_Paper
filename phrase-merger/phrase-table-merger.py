__author__ = 'amir'

org_phrase_table_addr='../../Phrase_Table/phrase-table.0-0.1.1'
lex_phrase_table_addr='../../Phrase_Table/phrase-table.lex'
vec_phrase_table_addr='../../Phrase_Table/phrase-table.vec'

phrase_4score_addr='phr4'
phrase_8score_addr='phr8'

p4=open(phrase_4score_addr,'w')
p8=open(phrase_8score_addr,'w')

org_phr=open(org_phrase_table_addr).readlines()
lex_phr=open(lex_phrase_table_addr).readlines()
vec_phr=open(vec_phrase_table_addr).readlines()

lex_dic={}
for line in lex_phr:
    toks=line.split('|||')
    scores=toks[2].split()
    lex_dic[toks[0].strip()+'|||'+toks[1].strip()]=(scores[0],scores[1])

vec_dic={}
for line in vec_phr:
    toks=line.split('|||')
    scores=toks[2].split()
    vec_dic[toks[0].strip()+'|||'+toks[1].strip()]=(scores[0],scores[1])


for line in org_phr:
    org_toks=line.split('|')
    key=org_toks[0].strip()+'|||'+org_toks[1].strip()
    try:
        score_lex=lex_dic[key]
        score_vec=vec_dic[key]
        temp=org_toks[2]
        org_toks[2]=score_vec[0].strip()+' '+score_lex[0].strip()+' '+score_vec[1].strip()+' '+score_lex[1].strip()
        p4.write((('|||').join(org_toks)).replace('\n','')+'\n')
        org_toks[2]=temp.strip()+' '+org_toks[2].strip()
        p8.write((('|||').join(org_toks)).replace('\n','')+'\n')
    except KeyError:
        print 'Not Found',line
        pass
