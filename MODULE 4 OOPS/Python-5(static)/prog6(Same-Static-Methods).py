# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent . m1() # How  to  call  m1()  method  of  parent  class
		#super() . m1()  #  Error :  super(No-args)  is  not  valid  in  static  method
		super(child , child) . m1()  # How  to  call  m1()  method  of  parent  class in   another way
		#self . m1() # Error :  No  self in  current  method  m1()
		#cls . m1() #  Error :   No  cls   in  current  method  m1()
		print('child  method')
#end of the class
parent . m1()  # How  to  call  m1()  method  of  parent  class
child . m1() # How  to  call  m1()  method  of  child  class


'''
parent method
parent method
parent method
child  method
'''