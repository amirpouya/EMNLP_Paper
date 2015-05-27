
import time
from createDic import createDict
import io


f = io.open('../../Phrase_Table/phrase-table.0-0.1.1',encoding="utf-8")
outp = io.open('outputAPAS.out','w',encoding="utf-8")

e2f = io.open('../../Vectors/words/new-lex.e2f',encoding="utf-8")
f2e = io.open('../../Vectors/words/new-lex.f2e',encoding="utf-8")


notF1 = 0.0000002
notF2 = 0.005 # when never has been in phrase Table
 
timeBefore = time.clock()
  
cd = createDict()
myDic = cd.creatDict(e2f,f2e)


 
del_line = '|'
del_dash = '-'

for line in iter(f):
       
        inpStr = line.split(del_line)
        
        sourc = inpStr[0].split()   # the first phrase foreign
        targ = inpStr[1].split()    # the second phrase English
            
        align = inpStr[3]
        alStr = align.split()
        lenS = len(sourc)
        lenT = len(targ)
        
    
        scores = [0] * lenS
        revScores  = [0] * lenT
        
        sizes = [0] * lenS
        revSizes = [0] * lenT
    
    
        # for the line's sentence
        for i in range(0,len(alStr)):
             
            # for the i'th alignment in lines th sentence
            soTotar = alStr[i].split(del_dash)
            so = int(soTotar[0])
            tar = int(soTotar[1])
            tupl = (sourc[int(so)],targ[int(tar)])

            if (tupl in myDic) :
                point = myDic[tupl]
                scores[so] += float(point[0])
                sizes[so] += 1
                revScores[tar] += float(point[1])
                revSizes[tar] += 1
            else:
                scores[so] += notF1
                sizes[so] += 1
                revScores[tar] += notF1
                revSizes[tar] += 1

         
                      
            
        lexicalWeight = 1.0000
        revLexicalWeight = 1.0000
        
        for i in range(0,lenS):
            if (sizes[i]==0):
                scores[i] = notF2
                sizes[i] = 1
    
            b = round( scores[i]*(1/sizes[i]),8)
            
            lexicalWeight *= b
          
            
        for i in range(0,lenT):
           
            if (revSizes[i]==0):
                revScores[i] = notF2
                revSizes[i] = 1
              
            
           
            a= round(revScores[i]*(1/revSizes[i]) ,8)
            revLexicalWeight *=a
        print (line)     
        outp.write(str(inpStr[0])+' ||| ' + str(inpStr[1])+' ||| '+str(max(round(lexicalWeight,8),0.00000001))+' '+str(max(0.00000001,round(revLexicalWeight,8)))+'\n')

   

timeAfter = time.clock()
print(timeAfter-timeBefore)



