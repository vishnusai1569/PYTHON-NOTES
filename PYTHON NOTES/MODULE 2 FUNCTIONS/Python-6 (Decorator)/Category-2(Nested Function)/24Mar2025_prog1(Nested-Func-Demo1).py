#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner() #  Executes  inner()  function
	print('Back  to  outer  function')
def  other():
	#inner()  # Error :  inner()  function  is  not  visible to  other  function  and  hence  can  not be  called
	print('Other  function')
# End  of  the  function
print('Begin')
outer()  #  Executes  outer()  function
print('Hi')
#inner()  # Error :  inner()  function  is  not  visible  outside and  hence  can  not be  called
other()  #  Executes  other()  function
print('Bye')


'''
Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
Other  function
Bye
'''
