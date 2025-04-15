'''
Write  a  program  to  add  two  lists  of  unequal  length  with comprehension

Let  1st  list  be  [10,20,30,40,50,60,70]  and  2nd  list  be  [100,200,300,400]
What  is   the  result ?  --->  [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[]
if len(k)>len(v):
       for i in range(len(v)):
              l=int(k[i]) + int(v[i])
              c.append(l)
else:
       for i in range(len(k)):
              l=int(k[i]) + int(v[i])
              c.append(l)
print(c)


