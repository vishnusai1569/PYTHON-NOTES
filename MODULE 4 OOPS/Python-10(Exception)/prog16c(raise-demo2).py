#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function')
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)   #  Throws  TypeError
	raise ValueError()
# end of  the function
try:
	print('Begin')
	f1(10)  # Throws  TypeError
	f1(20)  #  Skipped  due  to  error
	f1(30)  #  Skipped  due  to  error
	f1(0)  #  Skipped  due  to  error
except  ArithmeticError:
	print('Hyd');
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End')

'''
Begin
f1  function
Caught  TypeError  outside  the  function :  25
End
'''


'''
1) Execution  is  sequential  from  except  suite

2) Control  does  not  return  to  try  suite  after  execution  of  except  suite

3) Why  are  remaining  function  calls  f1(20) , f1(30)  and  f1(0)  not  executed ?  --->
																						Since  1st  function  call  to  f1()  raises  TypeError
'''