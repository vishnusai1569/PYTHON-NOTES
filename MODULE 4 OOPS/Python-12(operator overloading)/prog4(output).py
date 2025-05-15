# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def  __gt__(p , q):
		print('c1  class  __gt__  method : ' , p . x , q . x)
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  __gt__  method : ' , p . x , q . x)
#end of the class
a = c1(10)   #  Object  is  initialized  with  x =  10  by  constructor
b = c1(20)   #  Object  is  initialized  with  x =  20  by  constructor
a > b  #   Executes  __gt__()  method  of  class  c1   as   operand1  (i.e.  'a')  is  c1  class  object
a < b #   Executes  __gt__()  method  of  class  c1   as   operand1  (i.e.  'b')  is  c1  class  object  (a < b  is  interpreted  as  b >  a)
m = c2(30)   #  Object  is  initialized  with  x =  30  by  constructor
n = c2(40)   #  Object  is  initialized  with  x =  40  by  constructor
a < m  #   Executes  __gt__()  method  of  class  c2   as   operand1  (i.e.  'm')  is  c2  class  object  (a < m  is  interpreted  as  m >  a)
n < b  #   Executes  __gt__()  method  of  class  c1   as   operand1  (i.e.  'b')  is  c2  class  object  (n < b  is  interpreted  as  b >  n)




'''
c1  class  __gt__  method :  10 20
c1  class  __gt__  method :  20 10
c2  class  __gt__  method :  30 10
c1  class  __gt__  method :  20 40

What  is  the  key  to  execute  operator  overloading  method  ?  --->  Type  of   operand1
'''