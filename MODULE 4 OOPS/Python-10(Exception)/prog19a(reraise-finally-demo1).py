# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')    #  Skipped  due  to  raise
	except  KeyError:
		print('Caught  KeyError')
		raise  Exception()  #  Executes  finally  suite  before  Exception  is  caught  outside
	except:   #  Skipped  :  1st  except  suite  is  already  executed
		print('Sec')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')  #  Skipped  :  Exception  is  not  yet  caught
#End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')   #  Skipped :  Exception  is  not  yet  caught
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')

'''
Begin
f1  function
Caught  KeyError
f1's  finally
Recaught  Exception
Outside  finally
End  of  the  program
'''