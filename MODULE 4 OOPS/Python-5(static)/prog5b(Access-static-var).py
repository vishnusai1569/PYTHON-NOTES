# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1 . x) # How  to  print  static  variable  'x'
		print(self . x) # How  to  print  static  variable  'x'  in  another  way
		#print(x) #  Error :  No local variable   'x'
	def   m1(self):
		print(c1 . x) # How  to  print  static  variable  'x'
		print(self . x) # How  to  print  static  variable  'x'  in  another  way
		#print(cls . x) #  Error  :   No   cls  in  m1()  method
	@classmethod
	def   m2(cls):
		print(c1 . x) # How  to  print  static  variable  'x'
		print(cls . x) # How  to  print  static  variable  'x'  in  another  way
		#print(self . x) #  Error  :  No  self  on  m2()  method
	@staticmethod
	def   m3():
		print(c1 . x) # How  to  print  static  variable  'x'
		#print(cls . x) #  Error :  No cls  in  m3()  method
		#print(self . x) #  Error  :  No  self  in  m3()  method
# End  of  the  class
a =  c1()
print(c1 . x) # How  to  print  static  variable  'x'
print(a . x) # How  to  print  static  variable  'x'  in  another  way
#print(x) #  Error :   No  global  variable  'x'  in the program
#print(self . x) #  Error  :   No  self  outside  the  class
#print(cls . x) #   Error :  No  cls  outside  the class
a . m1() # How  to  call  method  m1()
c1 . m2() # How  to  call  method  m2()
c1 . m3() # How  to  call  method  m3()