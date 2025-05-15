'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  ---> pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->   Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
import   time , math
list = eval(input('Enter  list  of  radii  :   '))
m = map(lambda  r :  math . pi * r ** 2 , list)
print('Area  of  each  radius  in  the  list')
for  x  in  m:
	print(F'{x:.2f}')
	time . sleep(1)



'''
1) What  is  the  value  of  'r'  in  lambda  function  ?  ---> Each  element  of  the  list

2) Where  is  the  result  of  math . pi * r * r  returned  to ?  --->  for  loop  variable  'x'

3) How  to  define  regular  function  instead  of  lambda  function ?  --->  def   area(r):
																														 return  math . pi  * r * r

4) How  to  create  map  object  with  regular  function ?  ---> m = map(area , list)
'''