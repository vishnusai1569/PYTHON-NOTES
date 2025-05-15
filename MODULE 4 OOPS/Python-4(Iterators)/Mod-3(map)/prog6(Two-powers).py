# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)
import  time
m = map(lambda  x : 2 ** x , range(10))
print('Powers  of   2')
for  y  in  m:
	print(y)
	time . sleep(1)



'''
1) What  is  the  value  of  'x'  in  lambda  function ?  ---> Each  element  of  range  object  i.e.  0   to  9

2) Where  is  2 ** x   returned  to  ?  --->  for  loop  variable  'y'

3) How  to  define  regular  function  instead  of  lambda  function ?  ---> def   power(x):
																													     return  2 ** x

4) How  to  create  map  object  with  regular  function ?  --->  m = map(power , range(10))
'''