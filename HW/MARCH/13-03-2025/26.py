'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd is green city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
k=input("enter the strings:").split()
p=[[(k[i].upper()),(len(k[i]))] for i in range(len(k))]
print(p)
