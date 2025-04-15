# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)
#del  a[2]
#a . pop(2)
print(a)
print(id(a))
#How  to  remove  30  from  tuple  'a'
v=list(a)
v.pop(2)
print(tuple(v))
print(id(v))