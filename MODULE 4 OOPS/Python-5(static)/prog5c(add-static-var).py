# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10  	# How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1 . b = 20 # How  to  add  static  variable  'b'  with  value  20
		self. c = 30 # How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25 #  Error  :   No  cls  in  constructor
	def   m1(self):
		c1 . d = 40 # How  to  add  static  variable  'd'  with  value  40
		self . e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1 . f = 60 # How  to  add  static  variable  'f'  with  value  60
		cls . g = 70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25 #  Error :  No  self  in  m2()  method
	@staticmethod
	def   m3():
		c1 . h = 80 # How  to  add  static  variable  'h'  with  value  80
		#self . k = 25 #  Error :  No  self  in  m3()  method
		#cls . k = 35 #  Error :  No  cls  in  m3()  method
#End  of  the  class
print('Begin')
print(c1 . __dict__)  #  {'a' : 10}
print()
print()
x = c1()  #  Object  is  initialized  with  c = 30  by  constructor
print('Constructor')
print(c1 . __dict__)   #  {'a' : 10 , 'b' : 20}
print()
print()
x . m1()
print('Instance  method  m1')
print(c1 .__dict__)   #  {'a' : 10 , 'b' : 20 , 'd' : 40}
print()
print()
c1 . m2()
print('class  method   m2')
print(c1 . __dict__)   #  {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70}
print()
print()
c1 . m3()
print('static   method   m3')
print(c1 . __dict__)  #  {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h' : 80}
print()
print()
c1 . i = 90 # How  to  add  static  variable  'i'  with  value  90
x . j = 100 # How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)   #  {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h' : 80 , 'i' : 90}
print()
print()
print("Object  'x' ")
print(x . __dict__)  #  {'c' : 30 , 'e' :50 , 'j' : 100}


'''
static  variable  --->  a =  10 ,  b =  20 ,  d =  40 , f =  60 ,  g =  70 ,  h =  80 , i = 90

Object 'x'  --->  c =  30 ,  e = 50 ,  j =  100
'''