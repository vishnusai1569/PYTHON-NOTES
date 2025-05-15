# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')  #  Executes  finally  suite  before   ValueError  is  caught  outside  the  function
		print('Hi')  #  Skipped  due  to  raise
	finally:
		print("f1's  finally")
	print('End  of  f1  function') #  Skipped  : ValueError  is   not  yet  caught
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')
	finally:
		print("f2's  finally")
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg)
	finally:
		print("f3's  finally")
	print('End  of  f3  function')
def  f4():
	try:
		print("f4  function")
		sys . exit()
	finally:
		print("f4's  finally")
	print('End  of  f4  function')
#End  of  all  the  functions
try:
	print('Begin')
	f1() #   Throws  ValueError
	f2()  #  Skipped  :  ValueError  is  not  yet  caught
	f3()  #  Skipped : ValueError  is  not  yet  caught
	f4()   #  Skipped  :  ValueError  is  not  yet  caught
	print('Hello')   #  Skipped  :  ValueError  is  not  yet  caught
except  ValueError  as  msg:  # msg  is  'Hyd'
	print('ValueError  is  caught  outside :  ' , msg)
print('End  of  the  program')


'''
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :  Hyd
End  of  the  program
'''