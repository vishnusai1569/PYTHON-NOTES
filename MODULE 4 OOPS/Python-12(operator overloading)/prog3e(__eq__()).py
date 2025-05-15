# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __eq__(m , n):
		print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)  #  Object  is  initialized  with  x = 25   by  constructor
b = c1(25)  #  Object  is  initialized  with  x = 25  by  constructor
print(a == b)    #   __eq__()  method  prints  a  msg  and  returns   None   by  default
print(a != b)   #  Executes  __eq__()  method  becoz  a  !=  b  is  interpreted  as   not(a == b)  and  not  None   is  True
print(a . x !=  b . x) #   25  !=  25  is  False

'''
__eq__ method  :   25 25
None
__eq__ method  :   25 25
True
False


1) Why  is  __eq__()  method  not  executed  for  a . x  !=  b . x ?  --->  Since  25  and  25  are  integers  but  not  objects

2) Which  method  is  executed  for  a . x  !=  b . x ?  --->  __ne__()  method  of  int  class  becoz  25  and  25  are  integers
'''