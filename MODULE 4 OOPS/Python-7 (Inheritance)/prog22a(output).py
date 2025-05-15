# Find outputs  (Home  work)
class  parent:
	x = 100   #   static  variable
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super() . __init__()
		self . y = 20
	def disp(self):
		print(super() . x)
		print(self . x)
		print(self . y)
#end of the class
c = child() #  Object  is  initialized  with  x = 10 , y = 20  by  parent  and  child   constructors
c . disp()

'''
100
10
20


static  variable  ---> x = 100

object  'c'  --->   x=10 ,  y=20


1) Which  variable  is  accessed  for  super() . variable ?  --->  Static  variable  of  parent  class  due  to  super()

2) What  does  super() . variable  do  when  there  is  no  static  variable  in  the  parent  class ?  --->  Error

3) Can  super()  be  used  to  access  instance  variables ?  --->
														No  becoz  super()  means  to  parent  class  but  not  parent  class  object
'''