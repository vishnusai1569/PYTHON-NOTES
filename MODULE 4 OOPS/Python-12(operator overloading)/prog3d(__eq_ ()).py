# Find  outputs  (Home  work)
class   c1:
        def   __init__(self , y):
                self . x = y
        def    __eq__(m , n):
                print('__eq__ method  : ' , m . x , n . x)
                return  m . x == n . x
#end of the class
a = c1(10)   #  Object  is  initialized  with  x = 10 by  constructor
b = c1(20)   #  Object  is  initialized  with  x = 20 by  constructor
print(a == b)  #   __eq__()  method  prints  a  msg  and  returns   False  (10 ==  20  is  False)
print(a != b)   #  Executes  __eq__()  method  becoz  a  !=  b  is  interpreted  as   not(a == b)


'''
__eq__ method  :  10 20
False
__eq__ method  :  10 20
True


1) What  does  a != b  do  when  there  is  no  __ne__  method  in  the  class ? --->
																Executes  __eq__()  method  becoz  a != b  is  interpreted  as  not(a == b)

2) What  does  a !=  b  do  when  there  are  no   __ne__  and  __eq__()  methods  in  the  class  ?  --->  Compares  references
'''