# Find  outputs
try:
	print(7 / 0)  # Throws  ZDE
	print('Hello') #  Skiped  due  to  error
except  ZeroDivisionError:
	print('ZDE  1')  #  ZDE1
	try:
		print(8 / 0)   # Throws  ZDE
	except  ZeroDivisionError:
		print('ZDE   2')  #  ZDE2
	print('Bye')  #  Bye
except  ZeroDivisionError:  #  Skipped  becoz  1st  except  suite  is  already  executed
	print('ZDE  3')
print('End')  #  End

'''
ZDE  1
ZDE   2
Bye
End
'''

'''
1) How  many  except  suites  are  there  for  outer  try  suite ?  ---> 2

2) How  many  except  suites  are  there  for  inner  try  suite ?  --->  1
'''