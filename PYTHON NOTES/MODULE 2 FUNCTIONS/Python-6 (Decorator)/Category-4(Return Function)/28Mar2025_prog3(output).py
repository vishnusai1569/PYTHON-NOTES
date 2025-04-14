# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')
	def  inner1():
		print('1st  inner  function')
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")
	# End  of  inner2
	if   x == 10:
		return  inner1  #  Returned  to  outer(10)
	else:
		return  inner2   #  Returned  to  outer(20)
#end of the function
f1 = outer(10) #   f1 = inner1  --->  f1  points  to  inner1()  function
f2 = outer(20)  #   f2 = inner2  --->  f2  points  to  inner2()  function
f1() #  Executes  inner1()  function
f2()   #  Executes  inner2()  function


'''
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
'''
