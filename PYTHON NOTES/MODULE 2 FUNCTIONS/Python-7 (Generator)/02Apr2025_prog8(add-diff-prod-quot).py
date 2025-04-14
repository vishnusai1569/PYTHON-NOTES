'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
'''
import  time
def   f1(x , y):
	yield   F'Sum : {x + y}'
	yield   F'Differnece :  {x - y}'
	yield   F'Product :  {x * y}'
	try:
		yield   F'Division : {x / y }'
	except:
		yield  'Division  by zero  is  not  permitted'
# End  of  the  generator
a = eval(input('Enter   first  number  :   '))
b = eval(input('Enter   second  number  :   '))
g = f1(a , b)
for  k   in   g:
	print(k)
	time . sleep(2)



'''
1) Which  error  is  handled  by  for  loop  internally ?  --->  StopIteration  error

2) Does  for  loop  handle  ZeroDivisionError  internally ?  --->  No

3) Hence  ZeroDivisionError  needs  to  be  handled  explicitly
'''
