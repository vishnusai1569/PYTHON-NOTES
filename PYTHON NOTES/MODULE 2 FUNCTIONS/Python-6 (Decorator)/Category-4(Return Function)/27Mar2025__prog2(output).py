# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner #  Returns  inner  function  to  the  function  call  outer()
# End  of  the  function
fun = outer()  #  fun = inner  --->  Ref  fun  points to  inner()  function
print('Hello')
fun()  #  inner()  executes   inner()  function
print('Bye')
#inner() #  Error :  Not  visible  outside  and  hence  can  not  be  called


'''
Outer  Function
Hello
Inner function
Bye
'''
