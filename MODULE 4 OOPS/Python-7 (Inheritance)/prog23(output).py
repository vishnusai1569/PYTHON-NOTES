# Find outputs
class    parent:
	a = 10  #  How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     __init__(self):
		print('Parent  constructor')
		self . x = 20   # How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' , self . x)  #  How  to  print  variable  'x'
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,  parent . a) #  How  to  print  static  variable  'a'
		print('Parent  class  "class"  method  :  ' ,  cls . a)  # How  to  print  static  variable  'a'  in  another  way
		#print(self . a)  #   Error :  No  self  in  current  method  m2()
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  parent . a)  # How  to  print  static  variable  'a'
	def   __del__(self):
		print('parent  destructor  :  ' , self . x)  # How  to  print  variable  'x'
class  child(parent):
	b = 20  # How  to  add  static  variable  'b'  with  value  20
	def   __init__(self):
		super() . __init__()  #   How  to  call  parent  class  constructor
		print('Child  constructor')
		self . y = 40   #  How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super() . m1() #  How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method :  ' ,  self . y)  #  How  to  print  variable  'y'
	@classmethod
	def   m2(cls):
		parent . m2() #  How  to  call  m2()  method  of  parent  class
		super() . m2()  #  How  to  call  m2()  method  of  parent  class  in  another  way
		#cls . m2()  #   Error :  Method  of  same  class  is  executed  which  leads  to  recursion
		#self . m2()  #  Error :  No  self  in  current  method  m2()
		print('Child  class  "class"  method')
		print(parent . a) #  How  to  print  static  variable  'a'
		print(super() . a)  #  How  to  print  static  variable  'a'  in  another  way
		print(child . a)   #  How  to  print  static  variable  'a'  in  one  more  way
		print(cls . a)  #  How  to  print  static  variable  'a'  in  last  way
		print(child . b)  # How  to  print  static  variable  'b'
		print(cls . b)    #  How  to  print  static  variable  'b'  in  another  way
	@staticmethod
	def   m3():
		super(child , child) . m3()  #  How  to  call  m3()  method  of  parent  class
		#super() . m3()  #   Error :  super(no-args)  is  invalid  in  static  method
		#self . m3()  #  Error :  No  self  in  current  method  m3()
		#cls . m3()  #  Error :  No  cls  in  current  method  m3()
		print('child  class  static  method  :  ' ,  parent . a)  #  How  to  print  static  variable  'a'
		print(child . a)  #  How  to  print  static  variable  'a'  in  another  way
		print(child . b)   # How  to  print  static  variable  'b'
	def __del__(self):
		super() . __del__()   #  How  to  call  destructor  of  parent  class
		print('child  destructor  :  ' , self . y)  # How  to  print  variable  'y'
#end of the class
child . m2()  #  How  to  call  m2()  method  of  child  class
child . m3()  # How  to  call  m3()  method  of  child  class
c = child()
c . m1()  #    How  to  call  m1()  method  of  child  class



'''
1) How  to  call  parent  class  constructor  from  child  class ? --->


super() . __init__()

2) How  to  call  parent  class  instance  method  from  child  class ?  --->


super() . method()

3) How  to  call  parent  class  'class  method'  from  child  class  'class  method'  in  three  ways ?  --->


																									parent . method() , super() . method()  and  cls . method()

4) How  to  call  parent  class  static  method  from  child  class  static  method ?  --->


parent . method()

5) How  to  call  parent  class  destructor  from  child  class  destructor ? --->


super() . __del__()

6) What  are  the  two  ways  to  access  parent  class  static  variable  from  child  class  ? --->																																	super() . variable , parent . variable
'''