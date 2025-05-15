# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd') #  Skiped  due  to  raise
	except  KeyError:
		print('Caught  KeyError')
		raise   NameError()  #  Executes  finally  suite  before  NameError  is  caught  outside
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')  #  Skiped  :  NameError  is  not  yet   caught
#outside function
try:
	print('Begin')
	f1()
	print('Hello')  #  Skiped  :  NameError  is  not  yet   caught
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:   #  Executed  before  NameError   is   reported
	print('Outside  finally')
print('End of the program')  #  Skipped  :  NameError  is  not  caught

'''
Begin
f1  function
Caught  KeyError
f1 finally
Outside  finally
NameError  is   reported
'''