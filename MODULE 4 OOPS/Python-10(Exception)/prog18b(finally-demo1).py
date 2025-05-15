# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd') #  Executes  finally  suite  before  ValueError  is  caught  outside  the  function
		print('Hi') #   Skipped  due  to  raise
	finally:
		print("f1's  finally")
	print('End  of  f1  function')  #   Skipped  becoz  ValueError  is  not  yet  caught
def  f2():
	try:
		print('f2  function')
		return  #  Executes  finally  suite  before  control  moves  out  of   the  function
		print('Hello')  # Skipped  due  to  return
	finally:
		print("f2's  finally")
	print('End  of  f2  function')  # Skipped  due  to  return
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')  #   Skipped  due  to  raise
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)
	finally:
		print("f3's  finally")
	print('End of f3 function')
def  f4():
	try:
		print('f4 function')
		exit()   #  Executes  finally  suite  before  control  moves  out  of   the  program
	finally:
		print("f4's  finally")
	print('End of f4 function')  # Skipped  due  to  exit()
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello') #   Skipped  becoz  ValueError  is  not  yet  caught
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:   #  Executed  before  control  moves  out  of  the  program
		print('Outside  finally')
print('End  of  the  program')   # Skipped  due  to  exit()

'''
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :  Hyd
f2  function
f2's  finally
f3  function
Caught  by  f3  function :  25
f3's  finally
End of f3 function
f4 function
f4's  finally
outside  finally
'''