'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if
'''
import math
a = float(input('Enter  1st  side : '))  #  3
b = float(input('Enter  2nd  side : '))  #  4
c = float(input('Enter  3rd  side : '))  #  5
if a + b >= c  and  b + c >= a  and  c + a >= b:
	if a == b == c:
		print('Equilateral  triangle')
		area = math . sqrt(3) / 4 * a * a
		print(F'Area : {area:.2f}')
	elif  a == b  or  b == c  or  a == c:
		print('Isoscles  triangle')
		p = a + b + c
		print(F'Perimeter : {p}')
	else:
		print('Scalene  triangle')
		s = (a + b + c) / 2  #   6
		area = math . sqrt(s * (s - a) * (s - b) * (s - c))
		print(F'Area : {area:.2f}')
		print(F'Perimeter : {2 * s}')
else:
	print('Not  a  triangle')
