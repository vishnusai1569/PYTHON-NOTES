'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
try:
	x =  int(input('Enter  any  +ve  integer : '))
	y = 'Even  number'   if  x % 2 ==  0  else  'Odd  number'
	print(y)
except:
	print('Input  should  be  an  integer')




'''
1) What  is  the  issue  with  x % 2 = 0 ?  --->  opearand1  of  =  should  be  a  reference  but  x % 2  is  an  expression

2) Can  ==  0  be  omitted  from  x % 2 ==  0 ?  ---> Yes  but  the  messages  need  to  be  interchanged
																			     i.e. msg = 'Odd  Number'  if  x % 2   else  'Even  Number'
'''
