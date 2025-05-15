# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25)  #  Object  is  initialized  with  x = 25   by  constructor
b = c1(25) #  Object  is  initialized  with  x = 25   by  constructor
print(a != b)     #   __ne__()  method  prints  a  msg  and  returns  False  (25  !=  25  is  False)
print(a == b)  #   False  :   'a'  and  'b' point  to  different  objects
print(a  is  b)  #   False  :   'a'  and  'b' point  to  different  objects


'''
__ne__ method :   25 25
False
False
False


1) Which  method  is  executed  for  a == b  when  there  is  no  __eq__  method  in  the  class ? --->  No  method

2) What  does  a == b  do  when  there  is  no  __eq__()  method  in  the  class  ?  --->
																								Compares  references  i.e.  id's  of  objects

3) pre-defined-obj1 ==  pre-defined-obj2
    What  does   the  statement  do ?  --->  Compares  objects  due  to   __eq__()   method  in   pre-defined  classes

4) user-defined-obj1 ==  user-defined-obj2
    What  does  the  statement  do  when  there  is  no  __eq__()  method  in  the  class ? ---> Compares   references

5) How  to  compare  user-defined  objects  ? --->
													Overload  ==  operator  in  the  class  by  defining   __eq__()  method  in  the  class

6) What  does  is  operator  do ?  --->  Always  compares  references
															 (both  for  pre-defined  objects  and  also  for  user-defined  objects)
'''