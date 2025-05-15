'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
import  time
def   f1(start , end):
	while  start <=  end:
		yield  start
		start += 1
# End  of  generator
x = int(input('Enter  start  value :  '))
y = int(input('Enter  end  value :  '))
g = f1(x , y)
for  m  in   g:
	print(m)
	time . sleep(1)


'''
Why  is  sleep()  used  every  time ?  --->  To  give  an  impression  to  user  that  elements  are  generated  one  at  a   time
																  but  not  all  simultaneously
'''
