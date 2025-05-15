# Find  outputs  (Home  work)
try:
	print(7 / 0)  #  Throws  ZDE
	print('Hello')  # Skipped  due  to  error
except    ZeroDivisionError:  #  Caught  here
	print('ZDE  1')  #  ZDE1
	#print(8 / 0) #   Throws  ZeroDivisionError  which  can  not  be caught  and  error  is   reported
except    ZeroDivisionError:  #  Skipped  becoz  1st  except  is  already  executed
	print('ZDE  2')
print('Bye')  #  Bye



'''
1) When  can  error  be  handled ?  --->  When  it  is  raised  by  try  suite

2) When  can  an  error  be  not  handled ?  --->  When  it  is  raised  by  statement  outside  try  suite
'''