'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  --->  x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->   x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector . n = int(input('How  many  elements  : ')) # How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self . d = eval(input('Enter a list : '))# How  to  read  the  list  into  the  object
	def add(self , x , y):
		 self . d = []
		 for  i  in  range(vector . n):
				self . d . append(x . d[i] + y . d[i])  # How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector . get1() # How  to  call  get1()  method
a = vector()
a . get2() # How  to  read  the  list  into  1st  object  'a'
b = vector()
b . get2()  # How  to  read  the  list  into  2nd  object  'b'
c = vector()
c . add(a , b)  # How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print('Addition  results  :  '  , c.d)  # How  to  print  the  list  of  3rd   object