# Operator  overloading  demo  program
class  c1:
	def    __add__(x , y):
		return   'c1  class  objects  are  added'
	def   __sub__(self , m):
		return  'c1  class  objects  are  subtracted'
	def   __mul__(a , b):
		return  'cl  class  objects  are  multiplied'
	def   __truediv__(p , q):
		return   'cl  class  objects  are  divided   with  /'
	def   __floordiv__(self , k):
		return   'cl  class  objects  are  divided  with  //'
#end of the class
a = c1()
b = c1()
print(a + b) #   c1  class  objects  are  added
print(a - b)  # c1  class  objects  are  subtracted
print(a * b)  #  cl  class  objects  are  multiplied
print(a / b)   #  cl  class  objects  are  divided   with  /
print(a // b)   #  cl  class  objects  are  divided  with  //


'''
1) Are  a + b , a - b , a * b  , a / b and  a // b   expressions  (or)  method  calls  ? --->  Method  calls

2) Can  method  names  be  changed ?  --->  No  and  they  are  fixed

3) How  to  call  __add__()  method  in  another  way ?  --->  a . __add__(b)
    How  to  call  __sub__()  method  in  another  way ?  --->  a . __sub__(b)
    How  to  call  __mul__()  method  in  another  way ?  --->  a . __mul__(b)
    How  to  call  __truediv__()  method  in  another  way ?  ---> a . __truediv__(b)
    How  to  call  __floordiv__()  method  in  another  way ?  ---> a . __floordiv__(b)
'''