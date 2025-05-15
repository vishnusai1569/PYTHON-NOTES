# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')   # Skipped  due  to  raise
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError()   #  Executes  finally  suite  before   NameError   is   caught  outside
	except  NameError:  #  Skipped  :  1st  except  suite  is  already  executed
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')   # Skipped  :  NameError  is   not  yet  caught
#outside function
try:
	print('Begin')
	f1()
	print('Hello')   # Skipped  :  NameError  is   not  yet  caught
except ValueError:
	print('Hello')
except   Exception: #  NameError  is  caught here  becoz  Exception  is  parent  to  NameError
	print('Recaught  Exception')
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')
print('End of the program')

'''
Begin
f1  function
Caught  KeyError
f1 finally
Recaught  Exception
Outside  finally
End of the program
'''

'''
1) What  is  Exception  class  ?  --->  Parent  to   all   Error  classes

2) What  is  object  class  ?  --->  Parent  to  all   python  classes

3) What  is  ArithmeticError  class  ?  --->  Parent  to   ZDE  class
'''