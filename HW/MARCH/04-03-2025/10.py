a = b = c = 25
print(a , b , c)
del   a
print(b , c)
#print(a)#error a is deleted
del b
print(c)
print(b)#error b is deleted
del   c
print(c)#error c is deleted