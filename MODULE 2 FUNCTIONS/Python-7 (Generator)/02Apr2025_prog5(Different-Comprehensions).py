#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l) # [0 , 1 , 4 , 9 , 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}
print(s) # {0 , 1 , 4 , 9 , 16} can be any order
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}
print(d) #{0 : 0 , 1 : 1 , 2 : 4 , 3 : 9 , 4 : 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5))
print(g) # __str__() method   returns  type and address of the generator object
print(type(g)) # <class 'generator'>
