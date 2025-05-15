# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent . x) # How  to  print  variable  'x'
		print(self . x) # How  to  print  variable  'x'  in  another  way
		#print(x) # Error :  No  local variable  'x'  in  current  method  m1()
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(super() . x) # How  to  print  variable  'x'
		print(parent . x) # How  to  print  variable  'x'  in  another  way
		print(child . x) # How  to  print  variable  'x' in  one  more  way
		print(self . x)  # How  to  print  variable  'x' in  last  way
		print(child . y) # How  to  print  variable  'y'
		print(self . y) # How  to  print  variable  'y'  in  another  way
		#print(super() . y) #  Error :   No  variable  'y '  in parent class
		#print(y)  # Error :  No  local variable  'x'  in  current  method  m2()
# End  of child  class
p = parent()
p . m1()   # How  to  call   m1()  method  of  parent  class
c = child()
c . m2()  # How  to  call   m2()  method  of  child  class

'''
10
10
10
10
10
10
20
20
'''