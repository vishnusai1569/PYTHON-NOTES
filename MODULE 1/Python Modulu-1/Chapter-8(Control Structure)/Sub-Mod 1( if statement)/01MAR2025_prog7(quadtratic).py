'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  --->  b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  ---> (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  ---> (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  --->  3 - 4j
'''
import math
a = float(input('Enter  value  of  a : '))
if  a == 0:
	print('Value  of  a  can  not  be  0')
	exit()
b = float(input('Enter  value  of  b : '))
c = float(input('Enter  value  of  c : '))
disc = b ** 2 - 4 * a * c
if  disc > 0:
	print('Roots  are  real  and  distinct')
	root1 = (-b + math . sqrt(disc)) / (2 * a)
	root2 = (-b - math . sqrt(disc)) / (2 * a)
	print(F'Root 1 : {root1:.2f}')
	print(F'Root 2 : {root2:.2f}')
elif  disc < 0:
	print('Roots  are  imaginary  (or) complex')
	real = -b / (2 * a)
	imag= math . sqrt(-disc) / (2 * a)
	print(F'Root 1 : {real} +  {imag}j')
	print(F'Root 2 : {real} -  {imag}j')
else:
	print('Roots are real and equal')
	root = -b / (2 * a)
	print(F'Root 1 : {root}')
	print(F'Root 2 : {root}')
