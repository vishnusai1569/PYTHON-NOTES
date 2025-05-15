#  Find  outputs (Home  work)
def   decor(fun):#  fun  is  f1
	def   inner():
		print(F'Decorating  {fun . __name__}  function') #   f1
		fun()  # Executes  function  f1()
		print('Decoration  is  finished')
	return  inner #  Returned  to  function  call  decor(f1)
@decor #  Interpreted  as  f1 = decor(f1)  --->  f1 = inner  i.e.  f1  points to  inner()  function
def   f1():
	print('Hello')
# End  of  the  function
f1()  # Executes  inner()  function
print('Bye')

'''
Decorating  f1  function
Hello
Decoration  is  finished
Bye
'''
