# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  p . x + q .x
#end of the class
a = c1(10)  #  Object  is  initialized  with  x = 10  by  constructor
b = c1(20)  #  Object  is  initialized  with  x = 10  by  constructor
m = c1('10')  #  Object  is  initialized  with  x = '10'  by  constructor
n = c1('20')  #  Object  is  initialized  with  x = '20'  by  constructor
print('Sum : ' , a + b)   #  __add__()  method  of  class  c1  returns  30
print('Join : ' , m + n)   #  __add__()  method  of  class  c1  returns   '1020'


'''
object  a  --->   x = 10
object  b  --->   x = 20
object  m  --->  x = '10'
object  n  --->   x = '20'
'''