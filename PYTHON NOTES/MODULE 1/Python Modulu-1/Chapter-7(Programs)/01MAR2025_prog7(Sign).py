'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
try:
	x = float(input('Enter any number : '))
	y =  1  if  x > 0  else   -1   if  x < 0  else   0
	print('Result : ' ,  y)
except:
	print('Input  should  be  int  or  float   number')
