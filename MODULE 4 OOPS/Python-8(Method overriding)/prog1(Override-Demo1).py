#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()
x . m1()  # Executes  method  of  parent  class  as   'x'  points  to  parent  class  object
x = child()
x . m1()   # Executes  method  of  child  class  as   'x'  points  to   child  class  object

'''
Overridden  Method
Overriding  Method
'''