# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent . m1() # How  to  call  m1()  method  of  parent  class
		child . m1() # How  to  call  m1()  method  of  parent  class  in  another  way
		#super() . m1()  #  Error  :  super(No-args)  is  not  permitted  in  static  method
		super(child , child) . m1() # How  to  call  m1()  method  of  parent  class  in  another  way
		#self . m1() #  Error  :   No self  in  current  method  m2()
		#cls . m1() #  Error  :   No cls  in  current  method  m2()
		print('child  method')
#end of the class
parent . m1()  # How  to  call  m1()  method  of  parent  class
child . m2() #  How  to  call  m2()  method  of  child  class
child . m1()   #  Executes  method  of  parent  class  becoz  there  is   no  m1()  in  child  class

'''
parent  method
parent  method
parent  method
parent  method
child  method
parent  method



1) When  can  static  method  use  super() ?  --->   When  there  are   two  args  for   super()  function

2) Is  super()   valid  in  static  method  ?  --->   No  due  to  zero  args

3) Can  static  method  use  self , cls  and  super(No-args) ?  --->  No
'''