# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner #  Returned  to  function  call  outer('Hi')  (or)  outer('Hello')
# End  of  the  function
hi_fun = outer('Hi') #  hi_fun = inner  --->  hi_fun  points  to  inner()  function
hello_fun = outer('Hello')  #  hello_fun = inner  --->  hello_fun  points  to  inner()  function
hi_fun()  #  Executes inner()  function
hello_fun()  #  Executes inner()  function


'''
Hi
Hello
'''
