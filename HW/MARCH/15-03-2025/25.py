# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e)#{'a', 'A', 'm', ' ', 'o', 'R', 'r'}
#print(set(25))#error
print(set())#set()
