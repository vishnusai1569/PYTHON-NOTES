'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  --->  =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''
try:
	a = eval(input('Enter 1st input : '))
	b = eval(input('Enter 2nd input : '))
	c =  '>'  if  a > b  else  '<'  if  a < b  else  '='
	print('Result :  ' , c)
except  NameError:
	print('Input  string  should  be  in   quotes')
except  TypeError:
	print('Inputs  can  not  be  complex  numbers')
