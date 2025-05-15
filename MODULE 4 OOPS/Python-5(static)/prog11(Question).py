# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ?  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y' ? ---> instance variable
		z = 30   #  What  is   variable  'z' ?  ---> local variable
		c1 . m = 40   #  What  is  variable  'm' ? ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is  variable  'p' ? ---> instance variable
	c1 . q = 60   #  What  is  variable  'q' ? ---> static variable
	s = 70   #  What  is  variable  's' ? ---> local variable
#end of the function
k = 80   #  What  is  variable  'k' ? ---> global variable
c1 . l = 90   #  What  is  variable  'l' ? ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ? ---> instance variable


'''
1) Where  is  local  variable  initialized  ?  --->  Inside  function  and  method

2) Where  is  global  variable  initialized  ?  --->  Outside  function  and  class

3) Where  is  static  variable  initialized  ?  --->  Any  where  in  the  program  with  classname . variable = value

4) Where  is  instance  variable  initialized ?  --->  Any  where  in  the  program  with  obj . variable = value
'''