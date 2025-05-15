# Find  outputs
print((lambda   x  :   x * x) (7))  #  x is  7  and result is  49
print( lambda   x  :  x * x(7))  #   Type  and  address  of  lambda  function
print( lambda   x  :   x * x) #   Type  and  address  of  lambda  function
print( (lambda  x = 25 :  x * x) () )   #  x is  default  value  25  and result is   625
square = lambda  x :  x  *  x
print(square(5))   #  x is  5  and result is  25


'''
1) print((lambda  x :  x * x)(5))
    How  to  divide  the  above  statement  into  two  statements ?  ---> square = lambda  x  :  x * x  --->  Lambda  function  definition
																											   print(square(5))  --->   lambda  function  call

2) What  does  print(lambda  function)  do ?  --->  Prints  type  and  address  of  lambda  function

3) When  is  lambda  function  lost ?  ---> When  there  is  no  reference
    When  is  lambda  function  alive ?  ---> When  there  is  a   reference  to  the  function

4) print( lambda   x  :  x * x(7))
    What  are  multiplied ?  --->  x  and  result  of  x(7)
'''
