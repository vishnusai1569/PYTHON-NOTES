# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method  :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(10)    #  Object  is  initialized  with  x =  10  by  constructor
b = a  #   Ref  'b'  points  to  object  'a'
print(a != b)   #   __ne__()  method  prints  a  msg  and  returns  False  (10  !=  10  is  False)
print(a == b)   #  True  :  'a'  and  'b'  point  to  same  object


'''
__ne__ method  :   10 10
False
True
'''