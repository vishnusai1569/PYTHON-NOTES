# Find  outputs
class   c2:
	def  m1(self):
			print('Parent  Method')
class   c1(c2):  #  Valid :  parent  class  c2  exists
	def  m1(self):
			super() . m1()    #  Executes  method  of   parent  class  c2
			print('Child  Method')
class  c2(c1):  #  Valid :  parent  class  c1  exists
	def  m1(self):
			super() . m1()  #  Executes  method  of   parent  class  c1
			print('Grand  Child  Method')
a = c2()
a . m1()  #  Executes  method  of   grand  child  class  c2  as   'a' is  grand  child  object