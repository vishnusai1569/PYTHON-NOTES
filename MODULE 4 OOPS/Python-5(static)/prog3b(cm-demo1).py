# Find  outputs  (Home  work)
class   c1:
	x = 10  #  static  variable
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30  #  Modifies  static variable  'x'  to 30
		cls . y = 40   #  Adds  static  variable  'y'  to  class  c1  with  value   40
# End  of  the  class
a = c1() #   Object  is  initialized   with  y =  20  by  constructor
b = c1()   #   Object  is  initialized   with  y =  20  by  constructor
c1 . m1()
print(a . x) #  static   variable   becoz  there  is  no  a . x    i.e.  30
print(a . y) #  Variable  'y'  of  object  'a' i.e.  20
print(b . x) #  static   variable   becoz  there  is  no  b . x    i.e.  30
print(b . y)  #  Variable  'y'  of  object  'b'  i.e.  20
print(c1 . x , c1 . y) # 30 <space> 40
#print(cls . x , cls . y) #  Error  :   No  cls  outside  the  class
#print(self . x , self . y)   #  Error  :   No  self  outside  the  class


'''
static   variable   --->   x = 30 , y = 40

object  'a'   --->  y = 20

object  'b'   --->  y = 20



1) Which  variable  is  accessed  for  object . variable ? --->  Instance  variable

2) Which  variable  is  accessed  for  classname . variable ? --->  Static  variable

3) Which  variable  is  accessed  for  cls . variable ? --->  Static  variable

4) Can  self  and  cls  be  used  outside  the  class  ?  --->  No

5) Who  can  use  cls ?  --->  Only  class  method

6) Who  can  use  self ?  --->   Instnace  method , constructor  and  destructor
'''