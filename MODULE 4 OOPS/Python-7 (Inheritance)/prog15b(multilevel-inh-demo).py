#Multilevel  inheritance  demo  program
class  A:
	def    m1(self):
		print('class   A  method')
class  B(A):
	def  m1(self):
		print('class  B   method')
class   C(B):
	def  m1(self):
		print('class   C    method')
class   D(C):
	def   m1(self):
		print('class   D   method')
		super() . m1() # How  to  call  method  m1()  of  class  C
		super(C , self) . m1() # How  to  call  method  m1()  of  class  B  in  another  way
		super(B , self) . m1() # How  to  call  method  m1()  of  class  A  in  another  way
		#super(A , self) . m1() # Error :  No  m1()  method  in  object  class
		#super(C) . m1() # Error :  super()  function  can  not  take  single   arg
# End  of  the  class
d = D()
d . m1()  # How  to  call  method  m1()  of  class  D


'''
class   D   method
class   C    method
class  B   method
class   A  method
'''


'''
1) How  is  same  class  denoted ?  --->  self

2) How  is  parent  class  denoted ?  --->  super()

3) How  is  grandparent  class  denoted  ?  ---> super(parent-class-name , self)

4) How  is  greatgrandparent  class  denoted ?  --->  super(grandparent-class-name , self)
'''