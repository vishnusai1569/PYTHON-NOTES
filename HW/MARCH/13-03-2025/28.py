'''
(Home  work)
Repeat   previous  program  with  comprehension

Input1 : [10,20,30,40,50,60,70]
Input2 :  [100,200,300,400]
Output :  [110 , 220 , 330 , 440]
'''
k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
if len(k)>len(v):
    c=[k[i]+v[i] for i in range(len(v))]
else:
    c = [k[i] + v[i] for i in range(len(v))]
print(c)