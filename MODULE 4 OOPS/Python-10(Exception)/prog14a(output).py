# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')    #  f1  function
		print(7 / 0)  #  Throws  ZDE
	except  ValueError: #   Not  executed becoz  it  is  not  ZDE
		print('Hello')
	try:
		print(int('Ten'))
	except ZeroDivisionError:  #  Not  executed  becoz  it  is  not  for  1st  try  suite
		print('Bye')
	print('End  of  f1  function')  # Not  executed becoz  ZDE  is  not  yet  caught
# End of f1  function
try:
	print('Begin')  #  Begin
	f1()
	print('Hi')   # Not  executed becoz  ZDE  is  not  yet  caught
except  ZeroDivisionError:  #  Caught  here
	print('ZDE  is  caught  outside')  #  ZDE  is  caught  outside
except:  # Not  executed becoz 1st  except  suite  is  already  executed
	print('Bye')
print('End')  # End

'''
Begin
f1  function
ZDE  is  caught  outside
End
'''

'''
What  happens  when  f1()  throws  error   but  does  not  catch ?  --->   It  should  be  caught  outside  the  function
'''