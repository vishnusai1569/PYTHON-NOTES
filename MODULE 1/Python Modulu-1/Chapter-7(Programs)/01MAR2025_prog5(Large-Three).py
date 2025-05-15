'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Use  nested  ternary  operator
'''
try:
	a  = eval(input('Enter 1st input : '))
	b  = eval(input('Enter 2nd input : '))
	c =  eval(input('Enter 3rd input : '))
	max =   a  if  a > b   and  a > c  else  b  if  b > c   else  c
	print('Largest  Input  : ' , max)
except  NameError:
	print('Input  string  should  be  in  quotes')
except  TypeError:
	print('Input  can  not  be  complex  number')


'''
1) The  above  program  determines  largest  of  which  objects  ?  --->
								Any  object  except  complex  becoz  complex  numbers  can  not  be  compared  with  >  operator

2) max =  a   if  a > b  and  a > c  else  b  if  b > c  else  c
    What  does  1st  else  indicate ? --->  'a'  is  not  largest
    What  does  2nd  else  indicate ? ---> 'b'  is  also  not  largest
'''
