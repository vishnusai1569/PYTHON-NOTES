# reduce()  function  demo  program
from  functools  import  reduce
a = [10 , 20 , 15 , 12 , 5]
result = reduce(lambda  x , y :  x * y  , a)
print(result)  #  180000
print(type(reduce))  #  <class 'builtin_function_or_method'>



'''
1)  x              y         x * y
   -----------------------------------
    10           20          200
    200        15           3000
    3000      12           36000
    36000     5            180000

2) In  general , x  is  previous  result  and  y  is  next  element

3) How  to  define  regular  function  instead  of  lambda  function ?  --->  def  mul(x , y):
																															return  x * y

4) How  to  call  reduce()  function  with  regular  function ?  --->  result = reduce(mul , a)

5) The  above  reduce()  function  reduces  list  of  elements  to  a  single  element
      i.e.  Product  of  all  the  elements (180000)
'''