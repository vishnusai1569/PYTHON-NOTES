# Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi')
	inner2()   #  Executes  inner2()  function
	print('Hello')
	inner1()   #  Executes  inner1()  function
	print('Back  to  outer  function')
# End of the function
print('Begin')
outer()  #  Executes  outer()  function
print('Bye')


'''
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye
'''
