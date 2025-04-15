'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results
'''
import  math
try:
	a = int(input('Enter 1st  integer  number :  '))
	b = int(input('Enter 2nd  integer  number :  '))
	print(F'{a} + {b} = {a + b}')
	print(F'{a} - {b} = {a - b}')
	print(F'{a} * {b} = {a * b}')
	print(F'{a} / {b} = {a / b}')
	print(F'{a} % {b} = {a % b}')
	print(F'max({a} , {b}) = {max(a , b)}')
	print(F'min({a} , {b}) = {min(a , b)}')
	print(F'{a} ^ {b} = {a ** b}')
	print(F'sqrt({a}) = {math . sqrt(a)}')
	print(F'gcd({a} , {b}) = {math . gcd(a , b)}')
	print(F'fact({a}) = {math . factorial(a)}')
except:
	print('Input  should  be  integer  number')


'''
1) Where  are  gcd() , factorial()  and  sqrt()  functions  defined ?  --->  In  math  module

2) Where  are  max()  and  min()  functions  defined ?  ---> In  builtins  module

3) Can  inputs  be  float  numbers ?  --->  No  becoz  gcd  and  factorial  are  defined  only  for  integers
'''
