#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()  #  x = (10,20,30)
print(x)
print(type(x))
a , b , c =  f1()  # a , b , c =  (10,20,30)
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():   #  for  k  in   (10,20,30):
	print(k)


'''
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30
'''


'''
How  many  times  is  f1()  function  executed  in  the  program ?  --->  Thrice  becoz  it  is  called  thrice
'''
