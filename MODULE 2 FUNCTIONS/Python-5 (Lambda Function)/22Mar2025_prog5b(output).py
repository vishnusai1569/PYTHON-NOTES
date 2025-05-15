# Gift
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b #   It  is  a  tuple  of  4 elements
print(type(x))   #  <class  'tuple'>
print(x)#  (Type  and  address  of  lambda  function , 3 , 70 , 1.42)
for  y  in   x: #  'y'  is  each  element  of  tuple  'x'
	print(y) #  Type  and  address  of  lambda  function   <next  line> 3    <next  line>  70    <next  line> 1.42   <next  line>
print(x[0](9 , 2))  #  (lambda   a , b  :  a + b)(9 , 2) --->  11
print(x[1])  #  3
#print(x())  #  Error  :  'x'  is  not  a  function  but  tuple



'''
1) x = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
    Is  'x'  a  lambda  function  (or)  tuple ?  --->  A  lambda  function
    What  does  it  return ?  ---> Tuple  of  four  elements

2) x = lambda  a , b :  a + b ,  a - b , a * b , a / b
    Is  'x'  lambda  function  (or)  tuple ?  --->  Tuple  of  four  elements
    What  is  the  first  element  of  tuple ?  --->  lambda  a , b : a + b
    What  does  lambda  function  return ?  --->  Result  of  a + b
    What  about  a - b , a * b  and  a / b ?   --->  Remaining  elements  of  tuple
'''
