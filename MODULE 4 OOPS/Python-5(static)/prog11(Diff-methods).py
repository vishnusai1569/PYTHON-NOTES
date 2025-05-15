# Find  outputs
class  c1:
	def  m1(self):
		print('m1  method  of  class  c1')
class  c2:
	def  m1(self):
		print('m1 method of class c2')
class  c3:
	@classmethod
	def  m1(cls):
		print('m1 method of  class c3')
class  c4:
	@staticmethod
	def  m1():
		print('m1 method of  class c4')
class  c5(c1):
	def  m1(self):
		print('m1 method of class c5')
	def  m2(self):
		c3 . m1() # How  to  call  m1()  method  of  class  c3
		c4 . m1() # How  to  call  m1()  method  of  class  c4
		a = c2()
		a . m1() #How  to  call  m1()  method  of  class  c2
		super() . m1() # How  to  call  m1()  method  of  class  c1
		self . m1() # How  to  call  m1()  method  of  class  c5
		m1() # How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c = c5()
c . m2()  # How  to  call  m2()  method  of  class  c5


'''
m1 method of  class c3
m1 method of  class c4
m1 method of class c2
m1  method  of  class  c1
m1 method of class c5
m1 function
'''


'''
1) Call  m2()  method  which  inturn  calls  6  different  m1()  methods

2) How  to  call  method  of  same  class ?  --->  self . method()

3) How  to  call  method  of  parent  class ? ---> super() . method()

4) How  to  call  instance  method  of  different  class ? ---> object . method()

5) How  to  call  class  method (or) static  method  ? ---> classname . method()

6) How  to  call  function ? --->  function()
'''