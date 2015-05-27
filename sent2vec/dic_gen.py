__author__ = 'AmirPouya'
dic=open('test','w')
sum=49158
for i in range(0,sum):
    dic.writelines('sent_'+str(i)+' '+'sent_'+str(i)+'\n')
dic.close()
