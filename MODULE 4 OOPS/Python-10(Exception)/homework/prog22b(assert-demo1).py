'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  ---> Hyd <next line> End

2) What  is  the  output  if  input  is  25 ?  ---> Sec <next line> End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')