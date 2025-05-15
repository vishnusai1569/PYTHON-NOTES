# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1): #   Valid  : parent  class  c1  exists
	def  m1(self):
			super() . m1()   #  Executes  method  of   parent  class  c1
			print('Child  Method')
a = c1()
a . m1() #  Executes  method  of  child  class  c1  as  'a'  is  child  class   object


'''
Parent  Method
Child  Method
'''