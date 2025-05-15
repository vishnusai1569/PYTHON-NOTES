# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
#end of the class
a = c1(10) #  Object  is  initialized  with  x = 10 by  constructor
b = c1(20) #  Object  is  initialized  with  x = 20 by  constructor
print(a > b)#   __gt__()  method  prints  a  msg  and  returns   None
print(a < b)  #  Executes  __gt__()  method  becoz  a < b  is  interpreted  as  b > a


'''
__gt__ method  :  10   20
None
__gt__ method  :  20   10
None
'''


'''
1) What does  a < b  do  when  there  is  no  __lt__  method  in  the  class ? --->
															 Executes  __gt__()  method  becoz  a < b  is  interpreted  as  b >  a

2) What  does  a > b  do  when  there  is  no  __gt__  method  in  the  class ? --->
													Executes  __lt__()  method  becoz  a > b  is  interpreted  as  b <  a

3) What   does  a >  b  (or)  a < b  do  when  there  are  no  __gt__  and  __lt__()  methods  in  the  class  ?  --->
																																		Throws  error
'''