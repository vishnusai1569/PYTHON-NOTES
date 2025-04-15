'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
import math
x = float(input('Enter  value  of  x : '))  #  3
y = float(input('Enter  value  of  y : '))  #  4
r = float(input('Enter radius of circle : '))    #  5
d = math . sqrt(x ** 2 + y ** 2)  #  5
if d > r:
	print('Point is outside the circle')
elif d < r:
	print('Point is inside the circle')
else:
	print('Point is on the circle')
