# Find  outputs (Home  work)
def   f1():
	x = 'John'  # Lv  of  outer()  function
	def  f2():
		nonlocal  x  # Treats  'x'  as   variable  of   outer()  function
		x =  'Hello'  #  Modifies  Lv  of  outer()  function  to  'Hello'
	#end of inner function
	f2()
	return  x  #  Returns  'Hello'  to  function  call  f1()
#  End  of  f1()  function
print(f1()) #  Hello
