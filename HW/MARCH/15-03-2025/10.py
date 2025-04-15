# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100, 110, 120, 130, 140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10, 20, 15, 18)
e = tuple('Vamsi')#
print(e)#('V', 'a', 'm', 's', 'i')
#print(tuple(25))
print(tuple())#()