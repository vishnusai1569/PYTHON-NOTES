'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10,20,15,18,25,32]  and  2nd  list  be  [30,40,10,25,15]
What  is  the  output ?  ---> [20 , 18 ,  32]

Hint:  for  loop , if  cond , not  in  operator
'''

k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[]
for i in range(len(k)):
    if k[i] not in v:
        c.append(k[i])
print(c)
