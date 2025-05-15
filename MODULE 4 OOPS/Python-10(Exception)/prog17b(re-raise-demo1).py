#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)
		raise   ValueError(msg)
	except:  #  Not  executed  becoz   1st  except  suite  already  executed
		print('Hello')
	print('End  of  f1  function') #  Not  executed  becoz   ValueError  is  not  yet  caught
# End  of  f1()  function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')

'''
Begin
f1 function
Caught  by  f1 function  : 25
Recaught ValueError  :  25
End of the program
'''