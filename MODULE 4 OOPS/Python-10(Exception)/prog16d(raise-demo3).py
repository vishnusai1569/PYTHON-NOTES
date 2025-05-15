# Find  outputs  (Home  work)
def  f1(a):
	try:
		if   a == 10:
			raise  ValueError(25)
		elif   a == 20:
			raise  NameError(10.8)
		elif   a == 30:
			raise  IndexError('Hyd')
		raise  EOFError(True)
	except  IndexError  as  msg:
		print('Caught  IndexError  :  ' , msg)
	except ValueError  as  msg:
		print('Caught  ValueError  :  ' , msg)
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg)
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg)
	print('End  of  f1  function')
#outside the function
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')

'''
Caught  ValueError  :  25
End  of  f1  function
Caught   NameError  :  10.8
End  of  f1  function
Caught  IndexError  :  Hyd
End  of  f1  function
Caught   EOFError  :  True
End  of  f1  function
End of the program
'''


'''
Why  are  all  the  function  calls  executed  ?  --->  Since  f1()  function  is  not  only  rasing  error
													                              but  also  catching  the  error
'''