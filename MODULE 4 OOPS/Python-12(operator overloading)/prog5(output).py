# Overload  *  operator  to  multiply  2  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return  x . hr * y . noh
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  x . noh * y . hr
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)



'''
object  'a'  --->   empno = 25 , hr = 250
object  'b'  --->   empno = 25 , noh = 8


Which  class  method  is  executed  for  b *  a  when   __mul__()   method  of  class  c2  is  omitted ?  --->
																									Error  and  it  is  not  interpreted  as  a * b
'''