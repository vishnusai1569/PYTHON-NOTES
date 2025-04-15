# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,30,40}
print(type(c))#<type "class">
d = a ^ b
print(d)#{10, 50, 20, 60}
print(type(d))#<class 'set'>
print(c   is   d)#False
print(c  ==   d)#True