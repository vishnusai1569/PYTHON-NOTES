'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
a=input("enter the first string:") #java
b=input("enter the second string:")#Python
c=a[0:2]
d=a[2:]
e=b[0:2]
f=b[2:len(b)]
print(e+d," ",c+f)
