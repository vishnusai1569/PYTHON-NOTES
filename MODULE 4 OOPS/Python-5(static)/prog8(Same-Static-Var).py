# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent . x) # How  to  print  variable  'x'  of  parent  class
		print(self . x) # How  to  print  variable  'x'  of  parent  class  in  another  way
class   child(parent):
	x = 20
	def  m1(self):
		print(super() . x) # How  to  print  variable  'x'  of  parent  class
		print(parent . x) # How  to  print  variable  'x'  of  parent  class  in  another  way
		print(child . x) # How  to  print  variable  'x'  of  child  class
		print(self . x) # How  to  print  variable  'x'  of  child  class  in  another  way
# End  of  the  class
p = parent()
p . m1()# How  to  call  m1()  method  of  parent  class
c = child()
c . m1() # How  to  call  m1()  method  of  child  class


'''
10
10
10
10
20
20
'''