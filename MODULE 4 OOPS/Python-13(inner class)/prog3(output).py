# Find outputs (Home  work)
class  outer:
	def  __init__(self):  #  self  is  object  'o'
		self . x = 25
		self . y = self . inner1()   #  How  to  create  inner1  class  object
		self . z = self . inner2()   #  How  to  create  inner2  class  object
	def  disp(self):  #  self  is   object  o
		print(self . x)
	class   inner1:
		def  disp(self):  #  self  is   object   o . y
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):  #  self  is   object  o . z
			print('2nd  inner  class  method')
#end of the class
o = outer()
o . disp()  #   How  to  call   disp()  method  of outer  class
o . y . disp()  #  How  to  call   disp()  method  of inner1  class
o . z . disp()  #  How  to  call   disp()  method  of inner2  class


'''
object  'o'  --->   x = 25 ,  y =  empty  inner1  class  object  , z  =  empty  inner2  class  object


25
1st  inner  class  method
2nd  inner  class  method
'''