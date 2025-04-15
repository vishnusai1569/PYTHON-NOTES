'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

k=list(map(int,input("enter the elements in list1:").split(',')))
v=list(map(int,input("enter the elements in list1:").split(',')))
c=[k[i] for i in range(len(k)) if k[i] not in v]
print(c)