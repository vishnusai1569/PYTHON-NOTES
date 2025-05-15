''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->  Empty  string  <next line>  End

2) What  is  the  output  when  input  is  25 ?  ---> Sec <next line> End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')