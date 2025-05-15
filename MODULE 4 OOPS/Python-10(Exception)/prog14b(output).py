# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')  # f1  function
		print(7 / 0)  #  Throws  ZDE
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:   #  Caught  here
		print('ZDE  is  caught  by  f1  function')  #  ZDE  is  caught  by  f1  function
	print('End  of  f1  function') #   End  of  f1  function
#end of the  function
try:
	print('Begin')  # Begin
	f1()
	print('Hello')   # Hello
except  ZeroDivisionError:  #  Not  executed  becoz   ZDE  is  already  caught
 	print("Hi")
except  ValueError:
	print("Bye")
print('End')  # End

'''
Begin
f1  function
ZDE  is  caught  by  f1  function
End  of  f1  function
Hello
End
'''

'''
1) What  is  the  morale  of  the  program ?  ---> 
										If  a  function  throws  an  error,  it  should  be  caught  by  same  function  but  not  outside

2) What  happens  when  error  is  caught  outside ?  --->  Incorrect  results
'''