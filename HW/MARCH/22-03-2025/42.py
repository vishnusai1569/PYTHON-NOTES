# Find  outputs (Home  work)
def   f1():
	k = 'John'
	def  f2():
		nonlocal k
		k =  'Hello'
	#end of inner function
	f2()
	return  k
#  End  of  f1()  function
print(f1())
