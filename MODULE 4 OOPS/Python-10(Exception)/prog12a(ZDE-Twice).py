# Find  outputs  (Home  work)
try:
	print(7 / 0)  #  Throws  ZDE
	print('Hello')  #  Skipped  due  to   error
except    ZeroDivisionError:   #  Caught  here
	print('ZDE  1')  #  ZDE1
except    ZeroDivisionError:  #  Skipped  becoz  1st except  is  already  executed
	print('ZDE  2')
print('Bye')  #  Bye



'''
1) Can  same  error  be  handled  twice ?  --->  Yes  but  it  is  of  no  use

2) Which  except  suite  is  executed  when  same  error  is  handled  multiple  times ?  --->
																						First  except  suite  is  executed  and  rest  are  skipped
'''