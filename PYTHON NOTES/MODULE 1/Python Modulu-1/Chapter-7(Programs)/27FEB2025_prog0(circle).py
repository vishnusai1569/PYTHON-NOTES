'''
Write  a  program  to  determine  area  and  circumference  of  circle

1) What  is  the  input ?  --->  Radius

2) What  are  the  outputs ? --->  Area  and  circumference

3) What  is  the  area  of  circle ?  ---> pi * r ^ 2

4) What  is  the  circumference  of  circle ?  ---> 2 * pi * r
'''
import  math
try:
	r = float(input('Enter  radius  of  circle :  '))
	area = math . pi * r ** 2
	cir = 2 * math . pi * r
	print(F'Area :  {area:.2f}')
	print(F'Circumference :   {cir:.2f}')
except:
	print('Input  should  be  a  number')


'''
1)Read  inputs

2) Perform  computaions  on  inputs  and  derive  the  results

3) Print  results
'''
