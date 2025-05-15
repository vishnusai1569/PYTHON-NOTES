# Find  outputs   (Home  work)
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
#end of the class
x = parent()
x . m1()   # Executes   m1()  method  of  parent  class  as   'x'  points  to  parent  class  object
x . m2()   # Executes   m2()  method  of  parent  class  as   'x'  points  to  parent  class  object
#x . m3()  # Error :   No  m3()  method  in   parent  class
x = child()
x . m1()   # Executes  method  of  child  class  as   'x'  points  to  child  class  object
x . m2()     # Executes  method  of  parent  class  as   there  is  no  m2()  in  child  class
x . m3()      # Executes  method  of  child  class  as  'x'  points  to  child  class  object


'''
m1  method  of  parent  class
m2  method  of  parent class
m1  method  of  child  class
m2  method  of  parent class
m3  method  of  child  class
'''