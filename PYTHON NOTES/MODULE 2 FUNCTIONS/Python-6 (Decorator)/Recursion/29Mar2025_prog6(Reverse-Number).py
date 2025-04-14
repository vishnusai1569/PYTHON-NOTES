'''
Write  a   recursive  function  to  reverse  a  number

rev(678) =  678 % 10 * 10 ^ 2 + rev(678 // 10)
              =  800 + rev(67)
              =  800 + 67 % 10 * 10 ^ 1 + rev(67 // 10)
              =  800 + 70 + rev(6)
              =  800 + 70 + 6 % 10 * 10 ^ 0 + rev(6 // 10)
              =  800 + 70 + 6 + rev(0)
              =  800 + 70 + 6 + 0
			  = 876

1) How  many  function  calls  are  in  rev(678) ?  --->  4

2) How  many  function  calls  are  in  rev(n-digit number)  ? ---> n + 1

3) How  to  obtain  length  of a  number ?  --->  len(str(number))
'''
from math import *
def  rev(n):
	if  n > 0:
		return  n % 10 * 10 **  (len(str(n)) - 1) + rev(n // 10)
	else:
		return  0
'''
rev(946)  = 600 + rev(94)
               = 600 + 40 + rev(9)
               = 600 + 40 + 9 + rev(0)
               = 600 + 40 + 9 + 0
			   = 649
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))
