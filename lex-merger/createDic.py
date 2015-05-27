# the dictionary works in this way: the key contains two words, first is the foreign word second is the english word
# the value contains two float numbers, the first is the probability of translating from english to foreign and the second number is the probability of translation from foreign to english

class createDict:
    
    
    def creatDict(self,e2f,f2e):
        
        
        
        notF1 = 0.0000002   # when removed in pruning
        nF1DicC = 0;
       
        
        dic = dict()
     
       
        
        for line in iter(e2f):
            
            lineSpl = line.split()
            
            lineSpl0l = lineSpl[0]
            lineSpl1l = lineSpl[1]
            
            tupK = (lineSpl0l,lineSpl1l)
           
            tupV = (lineSpl[2],notF1)
            dic[tupK] = tupV
                  
        
        for line in iter(f2e):
            
            lineSpl = line.split()
            
            lineSpl0l = lineSpl[0]
            lineSpl1l = lineSpl[1]
            
            tupK = (lineSpl1l,lineSpl0l)
      
            if (tupK in dic):
                temp = dic[tupK]
              
                tupV = (temp[0] , lineSpl[2])
              
                dic[tupK] = tupV  
  
               
                
            else:
                tupV = (notF1,lineSpl[2])
                dic[tupK] = tupV
                nF1DicC +=1
                
                
    
        
        
        return dic