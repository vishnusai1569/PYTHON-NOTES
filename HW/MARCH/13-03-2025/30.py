'''
(Home  work)
Repeat   previous  program  with  comprehension

Inputs :  3  and  4

Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

k=int(input("enter no of rows:"))
m=int(input("rnter no of coloums:"))
x=[[0]*m for i in range(k)]
print(x)