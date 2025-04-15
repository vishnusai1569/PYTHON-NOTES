'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   ---> 20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Use   ternary  operator
'''
try:
	a  =  eval(input('Enter 1st input : '))
	b  =  eval(input('Enter 2nd input : '))
	max =   a   if  a > b  else  b
	print('Largest  Input  :  ' , max)
except  NameError:
	print('Input  string  should  be  in  quotes')
except  TypeError:
	print('Input  can  not  be  complex  number')


'''
The  above  program  determines  largest  of  which  objects  ?  --->
																			Any  Python  objects  except  complex  objects  becoz
																		    complex  objects  can  not  be  compared   with  >  operator
'''
