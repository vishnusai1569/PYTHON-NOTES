'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd is green city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]

Hint:  Use  split() , upper() , len()
'''
k=input("enter the strings:").split()
print(k)
p=[]
for i in range(len(k)):
    c=[]
    c.append(k[i].upper())
    c.append(len(k[i]))
    p.append(c)
print(p)