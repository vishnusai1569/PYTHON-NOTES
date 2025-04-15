'''
(Home  work)
program  with  comprehension

Input :  [hyd,pune,chennai,vijayawada]

Output :  ['H' , 'P' , 'C' , 'V']
'''
k=input("enter the elements:").split(',')
p=[k[i][0].upper() for i in range(len(k))]
print(p)
