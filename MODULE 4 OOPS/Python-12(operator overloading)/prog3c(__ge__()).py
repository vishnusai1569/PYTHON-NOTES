# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)  #  Object  is  initialized  with  x = 10 by  constructor
b = c1(20)  #  Object  is  initialized  with  x = 20 by  constructor
print(a >= b)  #   __ge__()  method  prints  a  msg  and  returns   False  (10 >=  20  is  False)
print(a <= b)   #  Executes  __ge__()  method  becoz  a <=  b  is  interpreted  as  b >= a

'''
__ge__ method :   10 20
False
__ge__ method :   20 10
True
'''


'''
1) What does  a <= b  do  when  there  is  no  __le__  method  in  the  class ? --->
															 Executes  __ge__()  method  becoz  a <= b  is  interpreted  as  b >=  a

2) What does  a >= b  do  when  there  is  no  __ge__  method  in  the  class ? --->
															 Executes  __le__()  method  becoz  a >= b  is  interpreted  as  b <=  a

3) What  does  a >=  b  (or) a <= b  do  when  there  are  no  __ge__  and  __le__()  methods  in  the  class  ?  ---> Throws  error
'''